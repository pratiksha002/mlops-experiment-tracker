import pandas as pd
from src.data_versioning import create_test_version

df = pd.DataFrame({
    "feature1": [1, 2, 3, 4],
    "feature2": [10, 20, 30, 40],
    "target": [100, 200, 300, 400]
})

version = create_test_version(df)

print("Version ID:", version)