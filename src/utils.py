"""
Utility functions for machine learning tasks
"""

import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns


def load_data(filepath):
    """
    Load data from CSV file
    
    Parameters:
    -----------
    filepath : str
        Path to the CSV file
        
    Returns:
    --------
    DataFrame
        Loaded data
    """
    return pd.read_csv(filepath)


def check_missing_values(df):
    """
    Check for missing values in the dataframe
    
    Parameters:
    -----------
    df : DataFrame
        Input dataframe
        
    Returns:
    --------
    DataFrame
        Summary of missing values
    """
    missing = pd.DataFrame({
        'Column': df.columns,
        'Missing_Count': df.isnull().sum().values,
        'Percentage': (df.isnull().sum() / len(df) * 100).values
    })
    return missing[missing['Missing_Count'] > 0].sort_values('Percentage', ascending=False)


def plot_distribution(data, column, bins=30):
    """
    Plot the distribution of a column
    
    Parameters:
    -----------
    data : DataFrame
        Input dataframe
    column : str
        Column name to plot
    bins : int
        Number of bins for histogram
    """
    plt.figure(figsize=(10, 4))
    plt.subplot(1, 2, 1)
    plt.hist(data[column], bins=bins, edgecolor='black', alpha=0.7)
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.title(f'Distribution of {column}')
    
    plt.subplot(1, 2, 2)
    plt.boxplot(data[column])
    plt.title(f'Boxplot of {column}')
    plt.ylabel(column)
    
    plt.tight_layout()
    plt.show()


def plot_confusion_matrix(y_true, y_pred, labels=None):
    """
    Plot confusion matrix for classification models
    
    Parameters:
    -----------
    y_true : array-like
        True labels
    y_pred : array-like
        Predicted labels
    labels : list, optional
        Label names
    """
    cm = confusion_matrix(y_true, y_pred)
    
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                xticklabels=labels, yticklabels=labels)
    plt.ylabel('True Label')
    plt.xlabel('Predicted Label')
    plt.title('Confusion Matrix')
    plt.show()
    
    print("\nClassification Report:")
    print(classification_report(y_true, y_pred, target_names=labels))


def normalize_features(X_train, X_test):
    """
    Normalize features to 0-1 range
    
    Parameters:
    -----------
    X_train : DataFrame or array
        Training features
    X_test : DataFrame or array
        Testing features
        
    Returns:
    --------
    tuple
        Normalized training and testing features
    """
    from sklearn.preprocessing import MinMaxScaler
    
    scaler = MinMaxScaler()
    X_train_normalized = scaler.fit_transform(X_train)
    X_test_normalized = scaler.transform(X_test)
    
    return X_train_normalized, X_test_normalized


def standardize_features(X_train, X_test):
    """
    Standardize features (zero mean, unit variance)
    
    Parameters:
    -----------
    X_train : DataFrame or array
        Training features
    X_test : DataFrame or array
        Testing features
        
    Returns:
    --------
    tuple
        Standardized training and testing features
    """
    from sklearn.preprocessing import StandardScaler
    
    scaler = StandardScaler()
    X_train_std = scaler.fit_transform(X_train)
    X_test_std = scaler.transform(X_test)
    
    return X_train_std, X_test_std


def print_model_performance(model, X_test, y_test, model_name="Model"):
    """
    Print model performance metrics
    
    Parameters:
    -----------
    model : sklearn model
        Trained model
    X_test : DataFrame or array
        Testing features
    y_test : array-like
        Testing labels
    model_name : str
        Name of the model
    """
    train_score = model.score(X_test, y_test)
    
    print(f"\n{model_name} Performance:")
    print(f"Accuracy: {train_score:.4f}")
    
    y_pred = model.predict(X_test)
    
    if hasattr(model, 'predict_proba'):
        print("(Classification model with probability predictions)")
    
    return train_score


if __name__ == "__main__":
    print("Utils module loaded successfully!")
    print("Available functions:")
    print("- load_data()")
    print("- check_missing_values()")
    print("- plot_distribution()")
    print("- plot_confusion_matrix()")
    print("- normalize_features()")
    print("- standardize_features()")
    print("- print_model_performance()")
