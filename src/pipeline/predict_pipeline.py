import sys
import pandas as pd
from src.utils import load_object
from src.exception import CustomException

class PredictPipelines:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            model_path = 'artifacts\model.pkl'
            preprocessor_path = 'artifacts\proprecessor.pkl'
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)
            data_scaled = preprocessor.transform(features)
            preds = model.predict(data_scaled)
            return preds

        except Exception as e:
            raise CustomException(e, sys)


class CustomData:
    def __init__(self,
                 SYMBOL: str,
                 OPEN: float,
                 HIGH: float,
                 LOW: float,
                 PREV_CLOSE: float,
                 LTP: float,
                 CHNG: float,
                 CHNG_PERCENT: float,
                 VOLUME: int,
                 VALUE: float,
                 W52_HIGH: float,
                 W52_LOW: float,
                 D30_PERCENT: float,
                 D365_PERCENT: float,
                 Daily_Return: float,
                 Volatility: float,
                 MA_7: float,
                 MA_30: float,
                 MA_50: float,
                 MA_200: float,
                 RSI: float,
                 Bid_Ask_Spread: float,
                 Volume_Ratio: float,
                 Risk_Category: str):
        self.SYMBOL = SYMBOL
        self.OPEN = OPEN
        self.HIGH = HIGH
        self.LOW = LOW
        self.PREV_CLOSE = PREV_CLOSE
        self.LTP = LTP
        self.CHNG = CHNG
        self.CHNG_PERCENT = CHNG_PERCENT
        self.VOLUME = VOLUME
        self.VALUE = VALUE
        self.W52_HIGH = W52_HIGH
        self.W52_LOW = W52_LOW
        self.D30_PERCENT = D30_PERCENT
        self.D365_PERCENT = D365_PERCENT
        self.Daily_Return = Daily_Return
        self.Volatility = Volatility
        self.MA_7 = MA_7
        self.MA_30 = MA_30
        self.MA_50 = MA_50
        self.MA_200 = MA_200
        self.RSI = RSI
        self.Bid_Ask_Spread = Bid_Ask_Spread
        self.Volume_Ratio = Volume_Ratio
        self.Risk_Category = Risk_Category

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "SYMBOL": [self.SYMBOL],
                "OPEN": [self.OPEN],
                "HIGH": [self.HIGH],
                "LOW": [self.LOW],
                "PREV. CLOSE": [self.PREV_CLOSE],
                "LTP": [self.LTP],
                "CHNG": [self.CHNG],
                "%CHNG": [self.CHNG_PERCENT],
                "VOLUME \n(shares)": [self.VOLUME],
                "VALUE": [self.VALUE],
                "52W H": [self.W52_HIGH],
                "52W L": [self.W52_LOW],
                "30 D   %CHNG": [self.D30_PERCENT],
                "365 D % CHNG \n 29-Sep-2022": [self.D365_PERCENT],
                "Daily Return": [self.Daily_Return],
                "Volatility": [self.Volatility],
                "7-Day MA": [self.MA_7],
                "30-Day MA": [self.MA_30],
                "50-Day MA": [self.MA_50],
                "200-Day MA": [self.MA_200],
                "RSI": [self.RSI],
                "Bid-Ask Spread": [self.Bid_Ask_Spread],
                "Volume Ratio": [self.Volume_Ratio],
                "Risk Category": [self.Risk_Category],
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)


# Example usage:
# Create a CustomData object with your data
custom_data = CustomData(
    Investment_Amount=int(input()),
    Risk_Category="Low"
)

# Get the data as a DataFrame
data_frame = custom_data.get_data_as_data_frame()

# Initialize a PredictPipelines object and make predictions
predictor = PredictPipelines()
predictions = predictor.predict(data_frame)

print(predictions)
