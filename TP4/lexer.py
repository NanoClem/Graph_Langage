"""
@author decoopmc
"""

import ply.lex as lex


#=============================================
#   LEXIQUE
#=============================================


# mots clés du langage
keywords = ['get', 'contains', 'excludes', 'and', 'or', 'http']
# mots de l'URL ou de l'URI
URwords  = [ 'HTTP1', 'NAME', 'DOT' ,'EXTENSION' ]

tokens = keywords + URwords


# definition des mots du langage
t_ignore    = ' \t'
t_get       = r'get'
t_contains  = r'contains'
t_excludes  = r'excludes'
t_and       = r'and'
t_or        = r'or'
t_http      = r'http'
t_HTTP1     = r'://'
t_DOT       = r'\.'
t_EXTENSION = r'html'


def t_NAME(t) :
    # """
    # Regex pattern et lexique pour les mots constituant la route de la page web,
    # soit les mots entre t_http et t_HTTP1, ou les mots suivant les contraintes \n
    # Si les mots sont dans 'keywords', leur nom est egal a leur valeur
    # :param t: token
    # :return: token t apres traitement pour le lexique
    # """
    r'\w+'                      # caracteres alphanumeriques
    if t.value in keywords :
        t.type = t.value
    return t


# Construction du lexique
lex.lex()


# Utilisation du lexique
def lex_data(d) :
    """
    Affiche les tokens correspondant a l'expression en parametre
    :d: expression du langage
    """
    lex.input(d)
    while True :
        tok = lex.token()   # Lecture du token suivant ou None
        if not tok : break
        print(tok)          # Affichage des tokens correspondant




#=============================================
#   TEST
#=============================================
if __name__ == '__main__':

    # Premier test
    print('TEST 1')
    data1 = 'get'      # fonctionne avec chaque mot dans 'keywords'
    lex_data(data1)

    # Deuxieme test
    print('TEST2')
    data2 = 'random'   # mot dans 'NAME'
    lex_data(data2)
