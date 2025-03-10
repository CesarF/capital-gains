from app.adapters.presenters.cli_presenter import CliPresenter
from app.adapters.repositories.account_repository import AccountRepository
from app.use_cases.base_use_case import BaseUseCase
from app.use_cases.operation_processors import calculate_sell_taxes, process_buy_operation
from app.use_cases.tax_calc_use_case import TaxCalculatorUseCase


def create_app():
    repository = AccountRepository()
    use_cases = {
        BaseUseCase: TaxCalculatorUseCase(
            repository, {
                'buy': process_buy_operation,
                'sell': calculate_sell_taxes
            }
        )
    }
    presenter = CliPresenter(use_cases)
    return presenter

# Avoid execution if this file is imported
if __name__ == '__main__':
    app = create_app()
    app.start()