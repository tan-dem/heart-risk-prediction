class FeatureEngineer:
    def __init__(self, df):
        self.df = df

    def add_features(self):
        self.df['bmi_age_interaction'] = (
            self.df['body_mass_idx'] * self.df['age']
        )
        self.df['diabetes_obesity'] = (
            self.df['diabetes'] * self.df['obesity']
        )
        self.df['pulse_blood_pressure'] = (
            self.df['systolic_blood_pressure']
            - self.df['diastolic_blood_pressure']
        )
        self.df['cardiac_marker_idx'] = (
            self.df['ck-mb'] + self.df['troponin']
        )
        self.df['cardio_history_scaled'] = (
            self.df['prev_heart_problems'] + self.df['medication']
        ) / 2
        self.df['activity_balance_scaled'] = (
            self.df['physical_activity_days_week'] / 7
            - self.df['sedentary_hrs_day'] + 1
        ) / 2
        self.df['lifestyle_risk_scaled'] = (
            self.df['smoking'] + self.df['alcohol']
            + (self.df['stress_level'] - 1) / 9 - self.df['sleep_hrs_day']
        ) / 3
        return self.df
