# encoding: utf-8
# module QuantConnect.Securities.Option calls itself Option
# from QuantConnect.Common, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc

# imports
import datetime
import Python.Runtime
import QuantConnect
import QuantConnect.Data
import QuantConnect.Data.Market
import QuantConnect.Orders
import QuantConnect.Orders.OptionExercise
import QuantConnect.Securities
import QuantConnect.Securities.Option
import System
import System.Collections.Concurrent
import typing

# no functions
# classes

class ConstantQLRiskFreeRateEstimator(System.object, QuantConnect.Securities.Option.IQLRiskFreeRateEstimator):
    """
    Class implements default flat risk free curve, implementing QuantConnect.Securities.Option.IQLRiskFreeRateEstimator.
    
    ConstantQLRiskFreeRateEstimator(riskFreeRate: float)
    """
    def Estimate(self, security: QuantConnect.Securities.Security, slice: QuantConnect.Data.Slice, contract: QuantConnect.Data.Market.OptionContract) -> float:
        pass

    @staticmethod # known case of __new__
    def __new__(self, riskFreeRate: float) -> None:
        pass


class CurrentPriceOptionPriceModel(System.object, QuantConnect.Securities.Option.IOptionPriceModel):
    """
    Provides a default implementation of QuantConnect.Securities.Option.IOptionPriceModel that does not compute any
                greeks and uses the current price for the theoretical price. 
                This is a stub implementation until the real models are implemented
    
    CurrentPriceOptionPriceModel()
    """
    def Evaluate(self, security: QuantConnect.Securities.Security, slice: QuantConnect.Data.Slice, contract: QuantConnect.Data.Market.OptionContract) -> QuantConnect.Securities.Option.OptionPriceModelResult:
        pass


class EmptyOptionChainProvider(System.object, QuantConnect.Interfaces.IOptionChainProvider):
    """
    An implementation of QuantConnect.Interfaces.IOptionChainProvider that always returns an empty list of contracts
    
    EmptyOptionChainProvider()
    """
    def GetOptionContractList(self, symbol: QuantConnect.Symbol, date: datetime.datetime) -> typing.List[QuantConnect.Symbol]:
        pass


class IOptionPriceModel:
    """ Defines a model used to calculate the theoretical price of an option contract. """
    def Evaluate(self, security: QuantConnect.Securities.Security, slice: QuantConnect.Data.Slice, contract: QuantConnect.Data.Market.OptionContract) -> QuantConnect.Securities.Option.OptionPriceModelResult:
        pass


class Option(QuantConnect.Securities.Security, QuantConnect.Interfaces.ISecurityPrice, QuantConnect.Securities.IDerivativeSecurity, QuantConnect.Interfaces.IOptionPrice):
    """
    Option Security Object Implementation for Option Assets
    
    Option(exchangeHours: SecurityExchangeHours, config: SubscriptionDataConfig, quoteCurrency: Cash, symbolProperties: OptionSymbolProperties, currencyConverter: ICurrencyConverter, registeredTypes: IRegisteredSecurityDataTypesProvider)
    Option(symbol: Symbol, exchangeHours: SecurityExchangeHours, quoteCurrency: Cash, symbolProperties: OptionSymbolProperties, currencyConverter: ICurrencyConverter, registeredTypes: IRegisteredSecurityDataTypesProvider, securityCache: SecurityCache)
    """
    def EvaluatePriceModel(self, slice: QuantConnect.Data.Slice, contract: QuantConnect.Data.Market.OptionContract) -> QuantConnect.Securities.Option.OptionPriceModelResult:
        pass

    def GetAggregateExerciseAmount(self) -> float:
        pass

    def GetExerciseQuantity(self, quantity: float) -> float:
        pass

    def GetIntrinsicValue(self, underlyingPrice: float) -> float:
        pass

    def GetPayOff(self, underlyingPrice: float) -> float:
        pass

    def IsAutoExercised(self, underlyingPrice: float) -> bool:
        pass

    def SetDataNormalizationMode(self, mode: QuantConnect.DataNormalizationMode) -> None:
        pass

    @typing.overload
    def SetFilter(self, minStrike: int, maxStrike: int) -> None:
        pass

    @typing.overload
    def SetFilter(self, minExpiry: datetime.timedelta, maxExpiry: datetime.timedelta) -> None:
        pass

    @typing.overload
    def SetFilter(self, minStrike: int, maxStrike: int, minExpiry: datetime.timedelta, maxExpiry: datetime.timedelta) -> None:
        pass

    @typing.overload
    def SetFilter(self, minStrike: int, maxStrike: int, minExpiryDays: int, maxExpiryDays: int) -> None:
        pass

    @typing.overload
    def SetFilter(self, universeFunc: typing.Callable[[QuantConnect.Securities.OptionFilterUniverse], QuantConnect.Securities.OptionFilterUniverse]) -> None:
        pass

    @typing.overload
    def SetFilter(self, universeFunc: Python.Runtime.PyObject) -> None:
        pass

    def SetFilter(self, *args) -> None:
        pass

    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, exchangeHours: QuantConnect.Securities.SecurityExchangeHours, config: QuantConnect.Data.SubscriptionDataConfig, quoteCurrency: QuantConnect.Securities.Cash, symbolProperties: QuantConnect.Securities.Option.OptionSymbolProperties, currencyConverter: QuantConnect.Securities.ICurrencyConverter, registeredTypes: QuantConnect.Securities.IRegisteredSecurityDataTypesProvider) -> None:
        pass

    @typing.overload
    def __new__(self, symbol: QuantConnect.Symbol, exchangeHours: QuantConnect.Securities.SecurityExchangeHours, quoteCurrency: QuantConnect.Securities.Cash, symbolProperties: QuantConnect.Securities.Option.OptionSymbolProperties, currencyConverter: QuantConnect.Securities.ICurrencyConverter, registeredTypes: QuantConnect.Securities.IRegisteredSecurityDataTypesProvider, securityCache: QuantConnect.Securities.SecurityCache) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    AskPrice: float

    BidPrice: float

    ContractFilter: QuantConnect.Securities.IDerivativeSecurityFilter

    ContractMultiplier: int

    ContractUnitOfTrade: int

    EnableGreekApproximation: bool

    ExerciseSettlement: QuantConnect.SettlementType

    Expiry: datetime.datetime

    IsOptionChain: bool

    IsOptionContract: bool

    OptionExerciseModel: QuantConnect.Orders.OptionExercise.IOptionExerciseModel

    PriceModel: QuantConnect.Securities.Option.IOptionPriceModel

    Right: QuantConnect.OptionRight

    StrikePrice: float

    Style: QuantConnect.OptionStyle

    Underlying: QuantConnect.Securities.Security

    SubscriptionsBag: System.Collections.Concurrent.ConcurrentBag[QuantConnect.Data.SubscriptionDataConfig]

    DefaultSettlementDays: int
    DefaultSettlementTime: TimeSpan


class OptionCache(QuantConnect.Securities.SecurityCache):
    """
    Option specific caching support
    
    OptionCache()
    """

class OptionDataFilter(QuantConnect.Securities.SecurityDataFilter, QuantConnect.Securities.Interfaces.ISecurityDataFilter):
    """
    Option packet by packet data filtering mechanism for dynamically detecting bad ticks.
    
    OptionDataFilter()
    """

class OptionExchange(QuantConnect.Securities.SecurityExchange):
    """
    Option exchange class - information and helper tools for option exchange properties
    
    OptionExchange(exchangeHours: SecurityExchangeHours)
    """
    @staticmethod # known case of __new__
    def __new__(self, exchangeHours: QuantConnect.Securities.SecurityExchangeHours) -> None:
        pass

    TradingDaysPerYear: int



class OptionHolding(QuantConnect.Securities.SecurityHolding):
    """
    Option holdings implementation of the base securities class
    
    OptionHolding(security: Option, currencyConverter: ICurrencyConverter)
    """
    @staticmethod # known case of __new__
    def __new__(self, security: QuantConnect.Securities.Option.Option, currencyConverter: QuantConnect.Securities.ICurrencyConverter) -> None:
        pass



class OptionMarginModel(QuantConnect.Securities.SecurityMarginModel, QuantConnect.Securities.IBuyingPowerModel):
    """
    Represents a simple option margin model.
    
    OptionMarginModel(requiredFreeBuyingPowerPercent: Decimal)
    """
    def GetLeverage(self, security: QuantConnect.Securities.Security) -> float:
        pass

    def SetLeverage(self, security: QuantConnect.Securities.Security, leverage: float) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, requiredFreeBuyingPowerPercent: float) -> None:
        pass

    RequiredFreeBuyingPowerPercent: float

class OptionPortfolioModel(QuantConnect.Securities.SecurityPortfolioModel, QuantConnect.Securities.ISecurityPortfolioModel):
    """
    Provides an implementation of QuantConnect.Securities.ISecurityPortfolioModel for options that supports
                default fills as well as option exercising.
    
    OptionPortfolioModel()
    """
    def ProcessExerciseFill(self, portfolio: QuantConnect.Securities.SecurityPortfolioManager, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order, fill: QuantConnect.Orders.OrderEvent) -> None:
        pass

    def ProcessFill(self, portfolio: QuantConnect.Securities.SecurityPortfolioManager, security: QuantConnect.Securities.Security, fill: QuantConnect.Orders.OrderEvent) -> None:
        pass


class OptionPriceModelResult(System.object):
    """
    Result type for QuantConnect.Securities.Option.IOptionPriceModel.Evaluate(QuantConnect.Securities.Security,QuantConnect.Data.Slice,QuantConnect.Data.Market.OptionContract)
    
    OptionPriceModelResult(theoreticalPrice: Decimal, greeks: Greeks)
    OptionPriceModelResult(theoreticalPrice: Decimal, impliedVolatility: Func[Decimal], greeks: Func[Greeks])
    """
    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, theoreticalPrice: float, greeks: QuantConnect.Data.Market.Greeks) -> None:
        pass

    @typing.overload
    def __new__(self, theoreticalPrice: float, impliedVolatility: typing.Callable[[], float], greeks: typing.Callable[[], QuantConnect.Data.Market.Greeks]) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    Greeks: QuantConnect.Data.Market.Greeks

    ImpliedVolatility: float

    TheoreticalPrice: float



class OptionPriceModels(System.object):
    """ Static class contains definitions of major option pricing models that can be used in LEAN """
    @staticmethod
    def AdditiveEquiprobabilities() -> QuantConnect.Securities.Option.IOptionPriceModel:
        pass

    @staticmethod
    def BaroneAdesiWhaley() -> QuantConnect.Securities.Option.IOptionPriceModel:
        pass

    @staticmethod
    def BinomialCoxRossRubinstein() -> QuantConnect.Securities.Option.IOptionPriceModel:
        pass

    @staticmethod
    def BinomialJarrowRudd() -> QuantConnect.Securities.Option.IOptionPriceModel:
        pass

    @staticmethod
    def BinomialJoshi() -> QuantConnect.Securities.Option.IOptionPriceModel:
        pass

    @staticmethod
    def BinomialLeisenReimer() -> QuantConnect.Securities.Option.IOptionPriceModel:
        pass

    @staticmethod
    def BinomialTian() -> QuantConnect.Securities.Option.IOptionPriceModel:
        pass

    @staticmethod
    def BinomialTrigeorgis() -> QuantConnect.Securities.Option.IOptionPriceModel:
        pass

    @staticmethod
    def BjerksundStensland() -> QuantConnect.Securities.Option.IOptionPriceModel:
        pass

    @staticmethod
    def BlackScholes() -> QuantConnect.Securities.Option.IOptionPriceModel:
        pass

    @staticmethod
    def CrankNicolsonFD() -> QuantConnect.Securities.Option.IOptionPriceModel:
        pass

    @staticmethod
    def Integral() -> QuantConnect.Securities.Option.IOptionPriceModel:
        pass

    __all__: list


class OptionStrategies(System.object):
    # no doc
    @staticmethod
    def BearCallSpread(canonicalOption: QuantConnect.Symbol, leg1Strike: float, leg2Strike: float, expiration: datetime.datetime) -> QuantConnect.Securities.Option.OptionStrategy:
        pass

    @staticmethod
    def BearPutSpread(canonicalOption: QuantConnect.Symbol, leg1Strike: float, leg2Strike: float, expiration: datetime.datetime) -> QuantConnect.Securities.Option.OptionStrategy:
        pass

    @staticmethod
    def BullCallSpread(canonicalOption: QuantConnect.Symbol, leg1Strike: float, leg2Strike: float, expiration: datetime.datetime) -> QuantConnect.Securities.Option.OptionStrategy:
        pass

    @staticmethod
    def BullPutSpread(canonicalOption: QuantConnect.Symbol, leg1Strike: float, leg2Strike: float, expiration: datetime.datetime) -> QuantConnect.Securities.Option.OptionStrategy:
        pass

    @staticmethod
    def CallButterfly(canonicalOption: QuantConnect.Symbol, leg1Strike: float, leg2Strike: float, leg3Strike: float, expiration: datetime.datetime) -> QuantConnect.Securities.Option.OptionStrategy:
        pass

    @staticmethod
    def CallCalendarSpread(canonicalOption: QuantConnect.Symbol, strike: float, expiration1: datetime.datetime, expiration2: datetime.datetime) -> QuantConnect.Securities.Option.OptionStrategy:
        pass

    @staticmethod
    def PutButterfly(canonicalOption: QuantConnect.Symbol, leg1Strike: float, leg2Strike: float, leg3Strike: float, expiration: datetime.datetime) -> QuantConnect.Securities.Option.OptionStrategy:
        pass

    @staticmethod
    def PutCalendarSpread(canonicalOption: QuantConnect.Symbol, strike: float, expiration1: datetime.datetime, expiration2: datetime.datetime) -> QuantConnect.Securities.Option.OptionStrategy:
        pass

    @staticmethod
    def Straddle(canonicalOption: QuantConnect.Symbol, strike: float, expiration: datetime.datetime) -> QuantConnect.Securities.Option.OptionStrategy:
        pass

    @staticmethod
    def Strangle(canonicalOption: QuantConnect.Symbol, leg1Strike: float, leg2Strike: float, expiration: datetime.datetime) -> QuantConnect.Securities.Option.OptionStrategy:
        pass

    __all__: list


class OptionStrategy(System.object):
    """
    Option strategy specification class. Describes option strategy and its parameters for trading.
    
    OptionStrategy()
    """
    Name: str

    OptionLegs: typing.List[QuantConnect.Securities.Option.OptionLegData]

    Underlying: QuantConnect.Symbol

    UnderlyingLegs: typing.List[QuantConnect.Securities.Option.UnderlyingLegData]


    OptionLegData: type
    UnderlyingLegData: type


class OptionSymbol(System.object):
    """ Static class contains common utility methods specific to symbols representing the option contracts """
    @staticmethod
    def GetLastDayOfTrading(symbol: QuantConnect.Symbol) -> datetime.datetime:
        pass

    @staticmethod
    def IsOptionContractExpired(symbol: QuantConnect.Symbol, currentTimeUtc: datetime.datetime) -> bool:
        pass

    @staticmethod
    def IsStandard(symbol: QuantConnect.Symbol) -> bool:
        pass

    @staticmethod
    def IsStandardContract(symbol: QuantConnect.Symbol) -> bool:
        pass

    @staticmethod
    def IsWeekly(symbol: QuantConnect.Symbol) -> bool:
        pass

    __all__: list


class OptionSymbolProperties(QuantConnect.Securities.SymbolProperties):
    """
    Represents common properties for a specific option contract
    
    OptionSymbolProperties(description: str, quoteCurrency: str, contractMultiplier: Decimal, pipSize: Decimal, lotSize: Decimal)
    OptionSymbolProperties(properties: SymbolProperties)
    """
    @staticmethod # known case of __new__
    @typing.overload
    def __new__(self, description: str, quoteCurrency: str, contractMultiplier: float, pipSize: float, lotSize: float) -> None:
        pass

    @typing.overload
    def __new__(self, properties: QuantConnect.Securities.SymbolProperties) -> None:
        pass

    def __new__(self, *args) -> None:
        pass

    ContractUnitOfTrade: int


