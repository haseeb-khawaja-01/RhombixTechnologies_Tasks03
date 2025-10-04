import matplotlib.pyplot as plt
import seaborn as sns

def plot_churn_distribution(df, save_path=None):
    plt.figure(figsize=(5,4))
    sns.countplot(x='Churn', data=df)
    plt.title('Churn Distribution')
    if save_path:
        plt.savefig(save_path, bbox_inches='tight')
    plt.show()

def plot_feature_importance(features, importances, top_n=20, save_path=None):
    import pandas as pd
    df = pd.DataFrame({'feature': features, 'importance': importances})
    df = df.sort_values('importance', ascending=False).head(top_n)
    plt.figure(figsize=(8,6))
    sns.barplot(x='importance', y='feature', data=df)
    plt.title('Top Feature Importances')
    if save_path:
        plt.savefig(save_path, bbox_inches='tight')
    plt.show()
