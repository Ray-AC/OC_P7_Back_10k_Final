from imports import *

async def tab_prediction_client_live(predict_df, final_dataframe, best_lgb, client_id: int):
    if client_id not in predict_df['sk-id-curr'].values:
        raise HTTPException(status_code=404, detail="Client ID not found")
    
    client_data = final_dataframe[final_dataframe['sk-id-curr'] == client_id].drop(columns=['target', 'sk-id-curr', 'index'])
    
    rounded_second_prediction_proba = np.round(best_lgb.predict_proba(client_data)[:, 1], 2).tolist()[0]
    
    prediction = (best_lgb.predict_proba(client_data)[:, 1] > 0.09).astype(int).tolist()[0] #0.09 = optimal_threshold
    
    combined_dict = {'prediction': prediction, 'Pourcentage de chance de remboursement': rounded_second_prediction_proba}
    return combined_dict