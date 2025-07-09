
# AI in Software Engineering Assignment

**Theme**: Building Intelligent Software Solutions  
**Objective**: Demonstrate AI applications in code generation, automated testing, and predictive analytics.

## 🛠️ Task Instructions

### Task 1: AI-Powered Code Completion
**Goal**: Compare manual vs AI-generated code for sorting dictionaries.  
**Files**:  
- [`sort_dicts.py`](task1/sort_dicts.py): Contains both implementations  
- [`analysis.md`](task1/analysis.md): Readability/efficiency comparison  

**How to Run**:
```bash
python task1/sort_dicts.py
```

---

### Task 2: Automated Login Testing
**Goal**: Test login page with valid/invalid credentials using Selenium.  
**Files**:  
- [`login_test.py`](task2/login_test.py): Automated test script  
- [`test_results.png`](task2/test_results.png): Execution proof  
- [`AI_testing_advantages.md`](task2/AI_testing_advantages.md): Benefits of AI in testing  

**How to Run**:
1. Install dependencies:
   ```bash
   pip install selenium
   ```
2. Execute:
   ```bash
   python task2/login_test.py
   ```

---

### Task 3: Breast Cancer Priority Prediction
**Goal**: Predict tumor priority (high/low) using Random Forest.  
**Files**:  
- [`breast_cancer_analysis.ipynb`](task3/breast_cancer_analysis.ipynb): Complete analysis  
- [`performance_metrics.md`](task3/performance_metrics.md): Model results  

**Key Steps**:
1. Preprocess images (resize to 128x128)
2. Train Random Forest classifier
3. Evaluate with accuracy/F1-score

---

## 📝 Report Contents (report.pdf)
1. **Theoretical Analysis**:
   - AI in code generation (GitHub Copilot)
   - Supervised vs unsupervised bug detection
   - Bias mitigation in UX personalization

2. **Ethical Reflection**:
   - Dataset biases in medical imaging
   - Fairness tools like IBM AI Fairness 360

---

## 🔧 Setup Guide
1. **Python Environment**:
   ```bash
   pip install -r requirements.txt  # Install all dependencies
   ```
   *(See [requirements.txt](#) for package versions)*

2. **Kaggle Dataset**:
   - Download from https://www.kaggle.com/competitions/iuss-23-24-automatic-diagnosis-breast-cancer/data 
   - Place `train.csv` in `task3/data/`

---

## 📊 Results Summary
| Task | Metric | Score |
|------|--------|-------|
| Task 1 | Code Efficiency | Equivalent O(n log n) |
| Task 2 | Test Accuracy | 100% pass rate |
| Task 3 | Model F1-Score | 0.77 |

---

## 🤖 AI Tools Used
- GitHub Copilot (Task 1)
- Selenium WebDriver (Task 2)
- Scikit-learn Random Forest (Task 3)
