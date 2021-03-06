"""
Constants used by the program.
"""

ROWS = 0
COLS = 1
DATA_PATH = "Data/diab_ckd_data.csv"

BLOOD_TEST_COLS = ["Creatinine_B_AT_BASELINE","Albumin_B_AT_BASELINE",
                   "Urea_B_AT_BASELINE","Glucose_B_AT_BASELINE","HbA1C_AT_BASELINE",
                   "RBCRed_Blood_Cells_AT_BASELINE","Hemoglobin_AT_BASELINE",
                   "Ferritin_AT_BASELINE","AST_GOT_AT_BASELINE","ALT_GPT_AT_BASELINE",
                   "Bilirubin_Total_AT_BASELINE","Na_Sodium_B_AT_BASELINE",
                   "K_Potassium_B_AT_BASELINE","CaCalcium_B_AT_BASELINE",
                   "HDLCholesterol_AT_BASELINE","LDLCholesterol_AT_BASELINE",
                   "Triglycerides_AT_BASELINE","PTH_AT_BASELINE"]

CLINICAL_COLS = ["IS_HYPERTENSION", "SE_HYPERTENSION", "IS_ISCHEMIC_MI",
                 "SE_ISCHEMIC_MI", "IS_CVA_TIA", "SE_CVA_TIA", "IS_DEMENTIA",
                 "SE_DEMENTIA", "IS_ART_SCLE_GEN", "SE_ART_SCLE_GEN",
                 "IS_TROMBOPHILIA", "SE_TROMBOPHILIA", "IS_IBD", "SE_IBD"]
