
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


### Preprocessing

1. **Filter Events by Category**
   - The first step involves filtering the data based on the `event_category` column. Specifically, we focus on separating purchase events from other events like `view` and `remove_cart`. This ensures that the data used for training the model is relevant to purchase behavior, which is typically the most significant for predictive modeling in e-commerce.

2. **Handle Null Values**
   - Next, we address any missing data within the dataset. It's crucial to check each column for null values, as missing data can negatively impact model performance. If null values are found, we replace them with the maximum value in the column or the most frequently occurring value (mode). This imputation strategy helps in maintaining the integrity of the data while preparing it for modeling.

3. **Convert Event Time to Event Date**
   - The `event_time` column, which likely contains timestamp data, is then converted into a more general event date format. This transformation simplifies the data and allows for easier analysis of trends over time, especially if the model will consider temporal patterns.

4. **Separate Brands and Products**
   - The dataset contains information about various brands and their products. In this step, we separate each brand and its associated products into distinct groups. This segmentation allows for more focused analysis and model training, where each brand-product combination can be individually evaluated and modeled. This approach is beneficial in scenarios where brand-specific trends or behaviors are of interest.

5. **Sampling the Data**
   - Finally, to optimize the preprocessing and evaluation process, only 10% of the original dataset is utilized. This sampling strategy is employed to manage computational resources effectively and to ensure that the preprocessing steps are applied efficiently without overwhelming the system. This sample should be representative of the entire dataset to ensure that the models trained on this data can generalize well to the full dataset.
<br>
<br

#### Output

<img width="1253" alt="forecasted" src="https://github.com/user-attachments/assets/67198611-11fd-44e9-8083-5079b38ff384">
<br>
<br>
<img width="1271" alt="viewer" src="https://github.com/user-attachments/assets/623bd23c-5bf1-4210-ada1-68799cf1df38">
