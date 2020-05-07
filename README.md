# Calculate RICE score

1. Make sure you have `ASANA_ACCESS_TOKEN` set in your env where you are running the script
1. Edit the file `get_custom_field_gids.py` and add the project id. Get the project ID from the url (https://app.asana.com/0/PROJECT_ID/list)
2. Run the script to retrieve the custom field settings
```bash
python3 get_custom_field_gids.py
```
3. Read through settings and identify gids for reach, impact, confidence, and effort
3. Make a copy of `project_values_sample.json` and rename to `project_values.json`
4. Add your values and custom field gids to `project_values.json`. If you've customized the numerical values for any of the custom fields, be sure to update those too! Remember we want to divide by Effort so the values that are multiplied should be 1/effort.
5. Run the calculation script!
```bash
python3 calculate_rice_score.py
```