
| **Step**                       | **Description**                                                                                                                                                           |
|--------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Input: Data**                | Collect data from Kaggle/Data sources.                                                                                                                                    |
| **Preprocessing**              | Process the data by removing unwanted columns and null values, converting timeseries to time data.                                                                         |
| **Developing a Predictive Model** | Start importing libraries and preparing the data for model creation. Convert the data into a supervised learning problem, then into batches of windows and horizon.        |
| **Selecting a Baseline Model** | Choose a baseline model to be used for comparison before creating other models. The metrics of the baseline model are considered optimal.                                   |
| **Model**                      | Create models and compare them with the baseline model.                                                                                                                   |
| **Evaluation Measures**        | Evaluate the created models using metrics such as Mean Absolute Error (MAE) and Root Mean Square Error (RMSE) to assess performance.                                       |
| **Best Model**                 | Select the best model based on the evaluation metrics.                                                                                                                    |
| **Output**                     | Display the results with visualization after selecting the best model based on the scores of the metrics.                                                                  |



![workflow](https://github.com/user-attachments/assets/359903a3-7a75-47f7-9429-3a8d36ed1260)




| **Category**        | **Details**                                                                                               |
|---------------------|-----------------------------------------------------------------------------------------------------------|
| **Source**          | [Rees46 Open CDP](https://rees46.com/en/open-cdp)                                                         |
| **Data Size**       | 14 GB                                                                                                     |
| **Rows**            | 20 million                                                                                                |
| **Columns**         | 9                                                                                                         |
| **Data Representation** | Each row represents an event                                                                           |
| **Dataset Features** | Event_time, Event_type, Product_id, Category_id, Category_code, Brand, Price, User_id, User_Transaction  |
| **Period Covered**  | October 2019 to December 2019                                                                             |
| **Data Description** | Dataset contains behavior data from a large multi-category online store. All events are related to products and users. Each event represents a many-to-many relation between products and users. |




![data](https://github.com/user-attachments/assets/8735d731-9d2e-4f3c-baca-9823bc19023b)
