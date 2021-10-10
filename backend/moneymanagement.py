#! /usr/bin/env python3
# coding: utf-8


class MoneyManagement:
    """Money management class"""

    def __init__(
        self,
        capital,
        percent_allowable_loss,
        risk,
        minimal_buy,
        take_profit,
        buy_price,
        stop_loss,
    ):
        """

        Args:
            capital (Float or Integer): Contains your capital
            take_profit (Float or Integer): Contains your stop profit
            buy_price (Float or Integer): Contains your buy price
            stop_loss (Float or Integer): Contains your stop loss
            percent_allowable_loss (Integer): Contains your percent allowable loss
            minimal_buy (Float or Integer): Contains your minimum purchase required by your trading platform
            risk (Integer): Contains your risk/reward ratio example risk = 2 for risk/reward 2:1
        """
        self.capital = capital
        self.take_profit = take_profit
        self.buy_price = buy_price
        self.stop_loss = stop_loss
        self.minimal_buy = minimal_buy
        self.risk = risk
        self.max_loss = self.calcul_max_loss(percent_allowable_loss)

    def calcul_risk(self):
        """Calculating the risk with your ratio choice

        Returns:
            Boolean: Return True your investment is safe / Return False if your investment isn't safe
        """
        if (self.take_profit - self.buy_price) >= (
            self.buy_price - self.stop_loss
        ) * self.risk:
            return True
        else:
            return False

    def calcul_max_loss(self, percent_allowable_loss):
        """Calculating your max loss money with your percent lost allocated or with your minimal buy

        Args:
            percent_allowable_loss (Integer): Contains your percent allowable loss

        Returns:
            Float: return your max money loss authorized
        """
        if self.capital * percent_allowable_loss / 100 > self.minimal_buy:
            return self.capital * percent_allowable_loss / 100
        else:
            return self.minimal_buy

    def calcul_buy_nb_action(self):
        """Calculating your number of cryptocurrency to buy

        Returns:
            Float: Return number of cryptocurrency
        """
        nb_action = self.max_loss / (self.buy_price - self.stop_loss)
        invest = self.max_loss / (self.buy_price - self.stop_loss) * self.buy_price

        if invest > self.capital:
            return round(self.capital / self.buy_price, 9)
        else:
            return round(nb_action, 9)

    def investment_price(self):
        """Calculating the price of the investment.

        Returns:
            Float: Returns the price of the investment to be made.
        """
        invest = self.max_loss / (self.buy_price - self.stop_loss) * self.buy_price
        if invest > self.capital:
            return round(self.capital, 2)
        else:
            return round(invest, 2)

    def envisaged_loss(self):
        """Calculating your loss envisaged

        Returns:
            Tuple: Amount envisaged loss and percent envisaged loss
        """
        loss = round(
            self.calcul_buy_nb_action() * self.stop_loss - self.investment_price(),
            2,
        )
        percent_loss = round(loss * 100 / self.capital, 2)
        return loss, percent_loss

    def envisaged_profit(self):
        """ "Calculating your profit envisaged

        Returns:
            Tuple: Amount envisaged profit and percent envisaged profit
        """
        profit = round(
            self.calcul_buy_nb_action() * self.take_profit - self.investment_price(),
            2,
        )
        percent_profit = round(profit * 100 / self.capital, 2)
        return profit, percent_profit


if __name__ == "__main__":
    pass
