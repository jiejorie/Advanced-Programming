# EXERCISE V: LAMDA FUNCTION
print("Lamda function")
marks = [("CodeLab I",67),("web Development", 75),("CodeLabII",74),("Smartphone Apps",68),("Games Development",70),("Responsive web",65)]
ascending = sorted(marks, key=lambda mark: mark[1])
descending = sorted(marks, key=lambda mark: mark[1], reverse=True)
print(f"\nLow to High:\n{ascending}\n\nHigh to Low:\n{descending}")