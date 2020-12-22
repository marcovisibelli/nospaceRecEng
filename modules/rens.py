
'''
Recomendation engine for no space
Copyright (c) 2020 by Marco Visibelli. All rights reserved.

'''

from .db import *
from .HybridLinUCB import *

# This rappresent a strategy
class rens():
    def __init__(self,name):
        self.name = name

        self.products = products_list.keys()

    # return the list of products
    def products_list(self):

        return [ {'id': key ,"name": products_list[key]['name'],"image": products_list[key]['image'],"problems": products_list[key]['problems'] } for key in self.products]

    def resolution(self,product_id,customer_id,problem_id):
        
        recommendation_matrix_data = recommendation_matrix[product_id][problem_id]

        lista = sorted(recommendation_matrix_data, key=lambda tup: tup[1],reverse=True)

        return lista[0]

    def feedback(self,product_id,customer_id,problem_id,response_id):
        
        recommendation_matrix_data = recommendation_matrix[product_id][problem_id]

        return True


    def select_resolution(self,product_id,resolution_id):

        return Resolutions_list[product_id][resolution_id] 
        