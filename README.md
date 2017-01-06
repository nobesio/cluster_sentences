# cluster_sentences
A minimal implementation of a clustering solution for spanish sentences based in Cosine Similarity and Affinity Propagation.

## Running the project

    $ python3 extract_clusters_from_text.py
    
## Some examples
Using the following senteces:

      sentences = [
          'Messi es el mejor jugador de Football.',
          'Neymar juega al football con Messi en el Barcelona.',
          'Los Pumas son la seleccion nacional de Rugby.',
          'Los Pumas ganaron contra Japon.',
          'Las Leonas ganaron una medalla de Oro en las olimpiadas.',
          'Carla Rebecchi es la capitana de las Leonas.'
      ]
      
I got:

      Messi es el mejor jugador de Football. :
        -  Messi es el mejor jugador de Football.
        -  Neymar juega al football con Messi en el Barcelona.
      Los Pumas ganaron contra Japon. :
        -  Los Pumas son la seleccion nacional de Rugby.
        -  Los Pumas ganaron contra Japon.
      Carla Rebecchi es la capitana de las Leonas. :
        -  Las Leonas ganaron una medalla de Oro en las olimpiadas.
        -  Carla Rebecchi es la capitana de las Leonas.

Quite neat, right?

## Author
Nicolás Martín Obesio, a computer science student at the University of Buenos Aires.

## Licence
MIT
