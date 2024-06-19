import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from imports import *
from tab.prediction import tab_prediction_client
from tab.prediction_live import tab_prediction_client_live

predict_df = pd.read_csv("./data/predict_10k_rows.csv")
final_dataframe = pd.read_csv("./data/final_dataframe_10k_rows.csv")
best_lgb = joblib.load('./data/best_lightgbm_model.pkl')

@pytest.mark.asyncio
async def test_prediction_client():
    test_pred_live = await tab_prediction_client_live(predict_df, final_dataframe, best_lgb, 100246)
    assert test_pred_live['Pourcentage de chance de remboursement'] == 0.59
    assert os.path.exists(os.path.join(os.path.join(os.path.dirname(__file__), '..', 'data'), 'report.html'))
    assert os.path.exists(os.path.join(os.path.join(os.path.dirname(__file__), '..', 'data'), 'interpratibilite_globale.png'))