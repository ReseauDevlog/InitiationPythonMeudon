# -*- coding: utf-8 -*-
import csv
import ballPack

def saveBalls(balls, filename, delimiter=','):
    """
    sauvegarde d'une liste de balles au format csv.

    Paramètres
    ----------

        balles    : liste à sauvegarder
        filename  : fichier de la sauvegarde
        delimiter : délimiteur entre chaque entrées
                    par défaut ','

    """

    with open(filename, 'w') as csvfile:
        ballwriter = csv.writer(csvfile, delimiter=delimiter,
                                quotechar='\\', quoting=csv.QUOTE_MINIMAL)
        for b in balls:
            class_name = str(b.__class__).split("'")[1]
            ballwriter.writerow([class_name, b.coords[0], b.coords[1], b.v[0], b.v[1], b.radius, b.domain[0], b.domain[1], '"' + b.color + '"'])

def readBalls(file, delimiter=','):
    """
    lit un fichier csv contenant une liste de balles et 
    renvoie cette liste en les contruisant.
    
    Paramètres
    ----------

        filename  : fichier de la sauvegarde
        delimiter : délimiteur entre chaque entrées
                    par défaut ','
    Sortie
    ------
    
        liste de balles

    """
    balls = []
    with open(file, 'r') as csvfile:
        ballreader = csv.reader(csvfile, delimiter=delimiter,
                                quotechar='\\', quoting=csv.QUOTE_MINIMAL)
        for row in ballreader:
            b = eval(row[0] + '(' + ','.join(row[1:]) + ')')
            balls.append(b)
    return balls

if __name__ == '__main__':
    import tempfile
    file = tempfile.NamedTemporaryFile()

    bin = [ball.BouncingBall(0, 1), ball.GravityBall(0, 1)]
    saveBalls(bin, file.name)
    bout = readBalls(file.name)
    
    print(bout)
