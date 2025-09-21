class DataPreprocessor:
    def __init__(self, df):
        self.df = df

    def drop_service_columns(self):
        self.df.drop(['Unnamed: 0'], axis=1, inplace=True)

    def rename_columns(self):
        rename_map = {
            'Age': 'age',
            'Cholesterol': 'cholesterol',
            'Heart rate': 'heart_rate',
            'Diabetes': 'diabetes',
            'Family History': 'family_history',
            'Smoking': 'smoking',
            'Obesity': 'obesity',
            'Alcohol Consumption': 'alcohol',
            'Exercise Hours Per Week': 'exercise_hrs_week',
            'Diet': 'diet_type',
            'Previous Heart Problems': 'prev_heart_problems',
            'Medication Use': 'medication',
            'Stress Level': 'stress_level',
            'Sedentary Hours Per Day': 'sedentary_hrs_day',
            'Income': 'income',
            'BMI': 'body_mass_idx',
            'Triglycerides': 'triglycerides',
            'Physical Activity Days Per Week': 'physical_activity_days_week',
            'Sleep Hours Per Day': 'sleep_hrs_day',
            'Blood sugar': 'blood_sugar',
            'CK-MB': 'ck-mb',
            'Troponin': 'troponin',
            'Gender': 'gender',
            'Systolic blood pressure': 'systolic_blood_pressure',
            'Diastolic blood pressure': 'diastolic_blood_pressure',
        }
        self.df.rename(columns=rename_map, inplace=True)

    def drop_missing_rows(self):
        self.df.dropna(subset=['diabetes'], inplace=True)

    def encode_gender(self):
        self.df['gender'] = self.df['gender'].map({
            'Female': 0,
            'Male': 1
        }).astype(int)

    def preprocess(self):
        self.drop_service_columns()
        self.rename_columns()
        self.drop_missing_rows()
        self.encode_gender()
        return self.df
