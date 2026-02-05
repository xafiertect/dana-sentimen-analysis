import pandas as pd
from google_play_scraper import Sort, reviews

app_id = 'id.dana'
TOTAL_REVIEW = 50000

result, _ = reviews(
    app_id,
    lang='id',
    country='id',
    sort=Sort.NEWEST,
    count=TOTAL_REVIEW
)
df = pd.DataFrame(result)


df_final = df[['content', 'score']].copy()
df_final.columns = ['review_text', 'rating']

file_name = 'dataset_dana.csv'
df_final.to_csv(file_name, index=False)

print(f"Berhasil mengumpulkan {len(df_final)} ulasan")
print(df_final.head())
print(df_final['rating'].value_counts().sort_index())
