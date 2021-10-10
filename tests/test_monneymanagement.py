#! /usr/bin/env python3
# coding: utf-8

from backend.moneymanagement import MoneyManagement

capital = 10000
take_profit = 1300
buy_price = 1000
stop_loss = 853
percent_allowable_loss = 1
minimal_buy = 15
risk = 2
money = MoneyManagement(
    capital,
    percent_allowable_loss,
    risk,
    minimal_buy,
    take_profit,
    buy_price,
    stop_loss,
)


def test_calcul_risk():
    assert money.calcul_risk() == True
    money.risk = 3
    assert money.calcul_risk() == False


def test_calcul_max_loss():
    assert money.calcul_max_loss(percent_allowable_loss) == 100
    assert money.calcul_max_loss(15) == 1500
    money.minimal_buy = 1000
    assert money.calcul_max_loss(percent_allowable_loss) == money.minimal_buy


def test_calcul_buy_nb_action():
    assert money.calcul_buy_nb_action() == 0.680272109
    money.capital = 1
    assert money.calcul_buy_nb_action() == 0.001
    money.capital = 10000


def test_investissement_price():
    assert money.investment_price() == 680.27
    money.capital = 1
    assert money.investment_price() == 1
    money.capital = 10000


def test_envisaged_loss():
    assert money.envisaged_loss() == (-100.0, -1.0)


def test_envisaged_profit():
    assert money.envisaged_profit() == (204.08, 2.04)
