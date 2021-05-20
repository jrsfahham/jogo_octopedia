import random


def linha(tam=50):
    return '=' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(50))
    print(linha())


def registro(n):
    nome = list()
    ponto = list()
    placar = list()
    for x in range(0, n):
        nome.append(str(input(f'Informe o nome do jogador {x + 1}\n>>')))
        placar.append(nome[x])
        ponto.append(0)
        placar.append(ponto[x])
    return placar


# IMPRIMIR NOME/PLACAR
def imprime_placar(m, n):
    cabecalho('Placar')
    print('Nome                       Pontos')
    for x in range(0, n * 2, 2):
        print(f'{m[x]:<21}', end='')
        print(f'{m[x + 1]:>7}')


def escolher_jogador(n):
    jog_esco = random.randrange(0, n * 2, 2)
    return jog_esco


def materia_disponivel(m):
    new_mat_disp = m
    return new_mat_disp


def fim_de_jogo(l):
    return l


def escolher_materia(j, p, m):
    mat_esco = random.choice(m)
    cabecalho('Roleta')
    print(f'Jogador sorteado: {p[j]}')
    print(f'Matéria sorteada: {mat_esco}')
    return mat_esco


def escolher_pergunta():
    pergunta = random.randrange(1, 11)
    return pergunta


def questoes(m, pr):
    if m == 'Hístoria':
        if pr == 1:
            print('[1] - Resposta 1')
            print('[2] - Resposta 2')
            print('[3] - Resposta 3')
            resp = int(input('Resp >> '))
            if resp == 1:
                return True

        if pr == 2:
            print('[1] - Resposta 1')
            print('[2] - Resposta 2')
            print('[3] - Resposta 3')
            resp = int(input('Resp >> '))
            if resp == 2:
                return True

        if pr == 3:
            print('[1] - Resposta 1')
            print('[2] - Resposta 2')
            print('[3] - Resposta 3')
            resp = int(input('Resp >> '))
            if resp == 3:
                return True

        if pr == 4:
            print('[1] - Resposta 1')
            print('[2] - Resposta 2')
            print('[3] - Resposta 3')
            resp = int(input('Resp >> '))
            if resp == 4:
                return True

        if pr == 5:
            print('[1] - Resposta 1')
            print('[2] - Resposta 2')
            print('[3] - Resposta 3')
            resp = int(input('Resp >> '))
            if resp == 5:
                return True

        if pr == 6:
            print('[1] - Resposta 1')
            print('[2] - Resposta 2')
            print('[3] - Resposta 3')
            resp = int(input('Resp >> '))
            if resp == 6:
                return True

        if pr == 7:
            print('[1] - Resposta 1')
            print('[2] - Resposta 2')
            print('[3] - Resposta 3')
            resp = int(input('Resp >> '))
            if resp == 7:
                return True

        if pr == 8:
            print('[1] - Resposta 1')
            print('[2] - Resposta 2')
            print('[3] - Resposta 3')
            resp = int(input('Resp >> '))
            if resp == 8:
                return True

        if pr == 9:
            print('[1] - Resposta 1')
            print('[2] - Resposta 2')
            print('[3] - Resposta 3')
            resp = int(input('Resp >> '))
            if resp == 9:
                return True

        if pr == 10:
            print('[1] - Resposta 1')
            print('[2] - Resposta 2')
            print('[3] - Resposta 3')
            resp = int(input('Resp >> '))
            if resp == 10:
                return True

    if m == 'Geografia':
        if pr == 1:
            print('[1] - Resposta 1')
            print('[2] - Resposta 2')
            print('[3] - Resposta 3')
            resp = int(input('Resp >> '))
            if resp == 1:
                return True

        if pr == 2:
            print('[1] - Resposta 1')
            print('[2] - Resposta 2')
            print('[3] - Resposta 3')
            resp = int(input('Resp >> '))
            if resp == 2:
                return True

        if pr == 3:
            print('[1] - Resposta 1')
            print('[2] - Resposta 2')
            print('[3] - Resposta 3')
            resp = int(input('Resp >> '))
            if resp == 3:
                return True

        if pr == 4:
            print('[1] - Resposta 1')
            print('[2] - Resposta 2')
            print('[3] - Resposta 3')
            resp = int(input('Resp >> '))
            if resp == 4:
                return True

        if pr == 5:
            print('[1] - Resposta 1')
            print('[2] - Resposta 2')
            print('[3] - Resposta 3')
            resp = int(input('Resp >> '))
            if resp == 5:
                return True

        if pr == 6:
            print('[1] - Resposta 1')
            print('[2] - Resposta 2')
            print('[3] - Resposta 3')
            resp = int(input('Resp >> '))
            if resp == 6:
                return True

        if pr == 7:
            print('[1] - Resposta 1')
            print('[2] - Resposta 2')
            print('[3] - Resposta 3')
            resp = int(input('Resp >> '))
            if resp == 7:
                return True

        if pr == 8:
            print('[1] - Resposta 1')
            print('[2] - Resposta 2')
            print('[3] - Resposta 3')
            resp = int(input('Resp >> '))
            if resp == 8:
                return True

        if pr == 9:
            print('[1] - Resposta 1')
            print('[2] - Resposta 2')
            print('[3] - Resposta 3')
            resp = int(input('Resp >> '))
            if resp == 9:
                return True

        if pr == 10:
            print('[1] - Resposta 1')
            print('[2] - Resposta 2')
            print('[3] - Resposta 3')
            resp = int(input('Resp >> '))
            if resp == 10:
                return True


def perg_disp_his(p):
    new_perg_dis_his = p
    return new_perg_dis_his


def perg_disp_geo(p):
    new_perg_dis_his = p
    return new_perg_dis_his


def perg_disp_bio(p):
    new_perg_dis_his = p
    return new_perg_dis_his


def perg_disp_cie(p):
    new_perg_dis_his = p
    return new_perg_dis_his


def perg_disp_art(p):
    new_perg_dis_his = p
    return new_perg_dis_his


def perg_disp_atu(p):
    new_perg_dis_his = p
    return new_perg_dis_his


def perg_disp_lgp(p):
    new_perg_dis_his = p
    return new_perg_dis_his


def perg_disp_ent(p):
    new_perg_dis_his = p
    return new_perg_dis_his


def pergunta_his(m, p, j, d):
    disponivel = perg_disp_his(d)
    perg_his = {1: 'Pergunta de Hístoria 1',
                2: 'Pergunta de Hístoria 2',
                3: 'Pergunta de Hístoria 3',
                4: 'Pergunta de Hístoria 4',
                5: 'Pergunta de Hístoria 5',
                6: 'Pergunta de Hístoria 6',
                7: 'Pergunta de Hístoria 7',
                8: 'Pergunta de Hístoria 8',
                9: 'Pergunta de Hístoria 9',
                10: 'Pergunta de Hístoria 10'}

    pr = escolher_pergunta()
    if pr in disponivel:
        perguntah = perg_his.get(pr)
        cabecalho(perguntah)
        if questoes(m, pr):
            cabecalho('VOCÊ ACERTOU')
            j += 1
            p[j] = p[j] + 1
            disponivel.remove(pr)
            perg_disp_his(disponivel)
            if not disponivel:
                return False
            return True
        else:
            cabecalho('VOCÊ ERROU!')
            perg_disp_his(disponivel)
            return True
    else:
        while pr not in disponivel:
            pr = escolher_pergunta()
            if pr in disponivel:
                perguntah = perg_his.get(pr)
                cabecalho(perguntah)
                if questoes(m, pr):
                    cabecalho('VOCÊ ACERTOU!')
                    j += 1
                    p[j] = p[j] + 1
                    disponivel.remove(pr)
                    perg_disp_his(disponivel)
                    if not disponivel:
                        return False
                    return True
                else:
                    cabecalho('VOCÊ ERROU!')
                    perg_disp_his(disponivel)
                    return True


def pergunta_geo(m, p, j, d):
    disponivel = perg_disp_geo(d)
    perg_geo = {1: 'Pergunta de Geografia 1',
                2: 'Pergunta de Geografia 2',
                3: 'Pergunta de Geografia 3',
                4: 'Pergunta de Geografia 4',
                5: 'Pergunta de Geografia 5',
                6: 'Pergunta de Geografia 6',
                7: 'Pergunta de Geografia 7',
                8: 'Pergunta de Geografia 8',
                9: 'Pergunta de Geografia 9',
                10: 'Pergunta de Geografia 10'}

    pr = escolher_pergunta()
    if pr in disponivel:
        perguntag = perg_geo.get(pr)
        cabecalho(perguntag)
        if questoes(m, pr):
            cabecalho('VOCÊ ACERTOU')
            j += 1
            p[j] = p[j] + 1
            disponivel.remove(pr)
            perg_disp_geo(disponivel)
            if not disponivel:
                return False
            return True
        else:
            cabecalho('VOCÊ ERROU!')
            perg_disp_geo(disponivel)
            return True
    else:
        while pr not in disponivel:
            pr = escolher_pergunta()
            if pr in disponivel:
                perguntag = perg_geo.get(pr)
                cabecalho(perguntag)
                if questoes(m, pr):
                    cabecalho('VOCÊ ACERTOU')
                    j += 1
                    p[j] = p[j] + 1
                    disponivel.remove(pr)
                    perg_disp_geo(disponivel)
                    if not disponivel:
                        return False
                    return True
                else:
                    cabecalho('VOCÊ ERROU!')
                    perg_disp_geo(disponivel)
                    return True
