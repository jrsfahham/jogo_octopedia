from Biblioteca import *

print(linha())
quant = int(input('Quantos jogadores irão participar?\n>> '))
print(linha())
placar = registro(quant)
print(linha())
materias = ['História', 'Geografia']
mat_disp = materia_disponivel(materias)

perg_dis_his = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
perg_dis_geo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
perg_dis_bio = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
perg_dis_cie = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
perg_dis_art = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
perg_dis_atu = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
perg_dis_lgp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
perg_dis_ent = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

dis_his = perg_disp_his(perg_dis_his)
dis_geo = perg_disp_geo(perg_dis_geo)
dis_bio = perg_disp_bio(perg_dis_bio)
dis_cie = perg_disp_cie(perg_dis_cie)
dis_art = perg_disp_art(perg_dis_art)
dis_atu = perg_disp_atu(perg_dis_atu)
dis_lgp = perg_disp_lgp(perg_dis_lgp)
dis_ent = perg_disp_ent(perg_dis_ent)

while True:
    # fim_game = fim_de_jogo(mat_disp)
    fim_game = mat_disp
    if not fim_game:
        cabecalho('FIM DO JOGO')
        imprime_placar(placar, quant)
        break
    jogador = escolher_jogador(quant)
    materia = escolher_materia(jogador, placar, mat_disp)

    if materia == 'História':
        fim = pergunta_his(materia, placar, jogador, dis_his)
        if not fim:
            mat_disp.remove('História')
            materia_disponivel(mat_disp)
            print(linha())

    if materia == 'Geografia':
        fim = pergunta_geo(materia, placar, jogador, dis_geo)
        if not fim:
            mat_disp.remove('Geografia')
            materia_disponivel(mat_disp)
            print(linha())
