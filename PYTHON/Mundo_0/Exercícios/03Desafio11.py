lista_produtos = {
    'PRODUTO': 'PlayStation',
    'VALOR': 4000,
}

desconto = 0.05
valor_final = lista_produtos['VALOR'] * (1 - desconto)

print(f"O valor do {lista_produtos['PRODUTO']} com desconto é R$ {valor_final:.2f}")