## Recommendation engine service for Nospace

questo servizio fornisce le informazioni al sistema AR tramite un API dettagliata come segue:


### Request

`GET /products`

ritorna la lista dei prodotti

`GET /product/<id_product>/<id_problem>`

ritorna la risoluzione al problema

`POST /product/<id_product>/<id_problem>/<id_status>`

permette di pushare lo status della risoluzione

