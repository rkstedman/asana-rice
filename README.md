# Calculate RICE score

1. Make sure you have `ASANA_ACCESS_TOKEN` set in your env where you are running the script
1. Edit the file `get_custom_field_gids.py` and add the project id. Get the project ID from the url (https://app.asana.com/0/PROJECT_ID/list)
2. Run the script to retrieve the custom field settings
```bash
python3 get_custom_field_gids.py
```
3. Read through settings and identify gids for reach, impact, confidence, and effort
4. Add values and custom field gids to `project_values.json`. Make sure that the value maps are correct for each custom field.
5. Run the calculation script!
```bash
python3 calculate_rice_score.py
```