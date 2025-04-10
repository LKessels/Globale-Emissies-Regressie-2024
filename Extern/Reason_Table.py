reason_counts = energy_data['reason'].value_counts().reset_index()

reason_counts.columns = ['Reden', 'Aanwezigheid']

print(reason_counts)