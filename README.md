# Product-Metrics-Dashboard.
Дашборд для отслеживания ключевых продуктовых метрик (DAU/MAU, Retention, Churn, LTV, CAC).
# Product Metrics Dashboard

Дашборд для Product Owner: DAU/MAU, Retention, LTV/CAC, выручка.

## Запуск
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Метрики
- **DAU** — daily active users
- **MAU** — monthly active users (30-дневное скользящее среднее)
- **Retention** — 1 - churned/DAU
- **LTV/CAC** — unit-экономика
