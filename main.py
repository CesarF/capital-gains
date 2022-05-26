from presenters.cli_presenter import CliPresenter
from repositories.capital_repository import CapitalRepository
from use_cases.base_use_case import BaseOperationUseCase
from use_cases.tax_calc_use_case import TaxCalculatorUseCase


def create_app():
    repository = CapitalRepository()
    use_cases = dict()
    use_cases[BaseOperationUseCase] = TaxCalculatorUseCase(repository)
    presenter = CliPresenter(use_cases)
    return presenter

if __name__ == "__main__":
    app = create_app()
    app.start()