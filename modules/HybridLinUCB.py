#!/usr/bin/env python3

'''
Main engine for recommedation system
Copyright (c) 2020 by Marco Visibelli. All rights reserved.
'''

import numpy as np
import math
import sys
from scipy import linalg
import datetime
import random
import statistics
import pickle

def Average(lst): 
    return sum(lst) / len(lst)

def probability(vector_a,final_proba):

    #print('->',vector_a)

    # the starting one in 1
    probabilita = 1
    
    for i,a in enumerate(vector_a):
        probabilita *= final_proba[i][a]
        
    #print(probabilita)
    proba = [ 0 if a >= ( probabilita *1000) else 1 for a in range(1000)]
    
    result = random.choice(proba)
    
    return probabilita,result

###############################
#
###############################
class Feature:
    def __init__(self,age =[[1],[1]],device =[[0.2,0.8],[0.2,0.8]],gender = [[1],[1]]):

        # Calcolo il numero di agenti
        self.x_feature_dict = {}

        # Probabilita' dato la timezone tempo
        self.proba_z = [0.3,0.6,0.7,0.5]

        # Conversion probaility
        self.proba_x = [age[0],device[0],gender[0]]

        self.proba_x_appear = [age[1],device[1],gender[1]]

        # viene calcolato dopo
        self.d_size = 0

        #dai parametri impostati
        self.z_size = len(self.proba_z)

        for age_x in range(0,len(age[0])):
            for device_x in range(0,len(device[0])):
                for gender_x in range(0,len(gender[0])):

                    # Passsandogli un bandit aggiunge l'agente all array agents e all'algoritmo) 
                    # Passa anche i parametri di ciascun agenete 
                    # Che sono   'minlight' , 'iota' e  'p'

                    self.d_size += 1

        agentID_counter = 0
        total_proba = 0

        for age_x in range(0,len(age[0])):
            for device_x in range(0,len(device[0])):
                for gender_x in range(0,len(gender[0])):

                    # Creo il vettore
                    feature = np.zeros(self.d_size)

                    # setto ad 1 
                    feature[agentID_counter] = 1

                    real_feature = [age_x, device_x,gender_x]
                    
                    # Calcolo la probabilita'
                    proba,_ = probability(real_feature,self.proba_x)

                    proba_appear,_ = probability(real_feature,self.proba_x_appear)

                    total_proba += proba_appear

                    self.x_feature_dict[agentID_counter] = [proba,proba_appear,feature.reshape((-1, 1)),real_feature]

                    #  agente id
                    agentID_counter +=1

        for are in self.x_feature_dict.keys():
            self.x_feature_dict[are][1] = self.x_feature_dict[are][1]/total_proba

    # return the proability of conversion, the proability to appear and the combination value
    def request_probability(self):
        
        return [(are[0],are[1],are[3]) for are in a.x_feature_dict.values()]


    def getZ(self):

        z_vector = np.zeros(4)

        now = datetime.datetime.now()

        hour = now.hour 

        if hour >=0 and hour <=8:
            hour_sele = 0

        elif hour >8 and hour <=12:
            hour_sele = 1

        elif hour >12 and hour <=18:
            hour_sele = 2

        else:
            hour_sele = 3

        z_vector[hour_sele] = 1

        z_vector = z_vector.reshape((-1, 1)) 

        return z_vector

    def getZ_random(self):

        z_vector = np.zeros(4)

        z_vector[random.randint(0,(len(z_vector)-1))] = 1

        z_vector = z_vector.reshape((-1, 1)) 

        return z_vector

    def getX_random(self):

        key,value_r = random.choice(list(self.x_feature_dict.items()))

        proba_x,proba_appear, x_vector,feature = value_r

        return key,x_vector,proba_x

    def getX(self,element):
    
        x_vector = element.split('-')

        x_vector_int = [int(ar) for ar in x_vector ]

        for i,are in enumerate(self.x_feature_dict.values()):
            #print('this: ', are[3],' vs ',x_vector_int)
            if are[3] == x_vector_int :
                #print('####>',i,'<#####')
                return are 

        return None


    def getX_V2M(self,Numero):
    
        ## converto alla vecchia maniera
        element = "0-"+str(Numero)+"-0"

        x_vector = element.split('-')

        x_vector_int = [int(ar) for ar in x_vector ]

        for i,are in enumerate(self.x_feature_dict.values()):
            #print('this: ', are[3],' vs ',x_vector_int)
            if are[3] == x_vector_int :
                #print('####>',i,'<#####')
                return are 

        return None
            

class HybridArm:
    #Representation of each arm. Has a set of arm-specific features of size d, common features k
    def __init__(self, id, d, k, alpha):
        self.id = id
        self.d = d
        self.k = k
        self.alpha = alpha
        #Li lines 8-10
        self.A = np.identity(self.d)
        self.B = np.zeros((self.d, self.k))
        self.b = np.zeros((self.d, 1))

    def getA(self):
        return self.A
    def getB(self):
        return self.B
    def getb(self):
        return self.b
    def getID(self):
        return self.id
    
    def getP(self, A0, b0, betaHat, z, x):

        #Li Lines 12-14, args are numpy arrays
        self.Ainv = linalg.inv(self.A)
        self.A0inv = linalg.inv(A0)
        self.thetaHat = np.dot(self.Ainv, self.b - np.dot(self.B, betaHat))
        self.x = x
        self.z = z
        
        #I have no doubt there is a better way to write these matrix products
        self.s1 = np.dot(np.transpose(z), np.dot(self.A0inv, z))
        self.s2 = np.dot(np.transpose(z), np.dot(self.A0inv, np.dot(np.transpose(self.B), np.dot(self.Ainv, x))))
        self.s3 = np.dot(np.transpose(x), np.dot(self.Ainv, x))
        self.s4 = np.dot(np.transpose(x), np.dot(self.Ainv, np.dot(self.B, np.dot(self.A0inv, np.dot(np.transpose(self.B), np.dot(self.Ainv, x))))))

        self.s = self.s1 - 2*self.s2 + self.s3 + self.s4 #Li line 13

        # Calcolo della proabilita' finale Z * beta + X * Theta 
        self.p = np.dot(np.transpose(z), betaHat) + np.dot(np.transpose(x), self.thetaHat) + self.alpha*np.sqrt(self.s)
        return self.p


    def getP_pure(self,theArm, A0, b0, betaHat, z, x):
        #print("theArm: ",theArm)
        #print("self.A",self.A)
        if hasattr(self, 'Ainv'):
            thetaHat = np.dot(self.Ainv, self.b - np.dot(self.B, betaHat))
            return np.dot(np.transpose(z), betaHat) + np.dot(np.transpose(x),thetaHat) * 100
        else:
            return [0]


    def update(self,reward,z,x):

        self.A += np.dot(x, np.transpose(x))
        self.B += x * z.T[0]
        self.b += reward * x
        
class HybridUCB:
    def __init__(self, ucb, env_feats):
        self.alpha = ucb; #upper bound coefficient, line 14 in the Li paper
        self.k = env_feats; #size of environment features common to all arms
        self.A0 = np.identity(self.k); #initialization of env features, line 1
        self.b0 = np.zeros((self.k,1)); #line 2
        self.z = np.zeros((self.k, 1))

        # probabilita' per ogni arm
        self.bestP = dict()

        #Maintain the set of arms in the system currently
        self.arms = dict()
        self.currentArm = None
    
    def load_status(self,status):
        return  pickle.loads(status)

    def save_status(self):
        return pickle.dumps(self, protocol=pickle.HIGHEST_PROTOCOL)

    #Todo: bulk add / remove 
    def addArm(self, id, d):
        #Add an arm to the system with unique ID id, with feature length fLen:
        self.arms[id] = HybridArm(id, d, self.k, self.alpha)

    def removeArm(self, id):
        try:
            del self.arms[id]
            #print 'Removed arm: ', id
        except KeyError:
            print('Attempted to remove nonexisted arm id', id)
            

    def update_pure(self,x,reward):
        #Call the arm-specific code

        return 1

        
    def select_pure(self,x):
        #Call the arm-specific code

        return 1


    def return_status(self, x_list):
        #Call the arm-specific code

        z_list = []

        # calcolo dello z (usato dopo per scorrere)
        for a in range(4):
            z_vector = np.zeros(4)
            z_vector[a] = 1
            z_list.append((a,z_vector))


        self.betaHat = np.dot(linalg.inv(self.A0), self.b0)

        #Quello dettagliato
        bestP_a = dict()
        bestP_summa = dict()
        bestP_value = 0

        #print('--> self.A0 <--',self.A0)

        # PER TUTTI GLI x
        for x_vector_t in x_list:

            #print('x_vector_t ->',x_vector_t)

            x = x_vector_t[1][2].reshape((-1, 1)) 

            #print('x_vector_t[0] ->',x_vector_t[0])

            bestP_a[x_vector_t[0]] = dict()  
            bestP_summa[x_vector_t[0]] = dict()  

            # per tutti a 4 gli arm
            for theArm in self.arms:
                lista = []

                # Lo calcola indipendentemente dallo Z
                for z_i,z in z_list:
                    vale = self.arms[theArm].getP_pure(theArm,self.A0, self.b0, self.betaHat, z, x)
                    bestP_a[x_vector_t[0]][(theArm,z_i)] = vale
                    lista.append(float(vale[0]))

                value_calc = Average(lista)

                if value_calc > bestP_value:
                    bestP_value = value_calc

                bestP_summa[x_vector_t[0]][theArm] = value_calc

        return bestP_value,bestP_summa

    def select(self, z, x):
        #Call the arm-specific code

        self.z = z
        self.x = x

        self.betaHat = np.dot(linalg.inv(self.A0), self.b0)
        bestP = dict()

        for theArm in self.arms:
            bestP[theArm] = self.arms[theArm].getP(self.A0, self.b0, self.betaHat, z, x)

        self.currentArm = self.arms[max(bestP, key=lambda k: bestP[k])]

        return self.currentArm.getID()
        
    def update(self, reward,arm_sele,z,x):
        #The class is stateful - expects the self.currentArm to have been pulled and produced a real-valued reward
        #lines 17-18
        self.A0 += np.dot(np.transpose(self.arms[arm_sele].getB()),  np.dot(linalg.inv(self.arms[arm_sele].getA()), self.arms[arm_sele].getB()))
        self.b0 += np.dot(np.transpose(self.arms[arm_sele].getB()), np.dot(linalg.inv(self.arms[arm_sele].getA()), self.arms[arm_sele].getb()))

        #Update the arm-specific matrices: lines 19-21
        self.arms[arm_sele].update(reward,z,x)

        #Update the general matrices again: lines 22-23
        self.A0 += np.dot(z, np.transpose(z))
        self.A0 -= np.dot(np.transpose(self.arms[arm_sele].getB()), np.dot(linalg.inv(self.arms[arm_sele].getA()), self.arms[arm_sele].getB()))

        self.b0 += reward * z
        self.b0 -= np.dot(np.transpose(self.arms[arm_sele].getB()), np.dot(linalg.inv(self.arms[arm_sele].getA()), self.arms[arm_sele].getb()))