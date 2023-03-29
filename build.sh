 #!/bin/bash

# Activate the "game" virtual environment
source linkedin-github/bin/activate

# Run the "main.py" file
python src/main.py < input.txt

# Deactivate the virtual environment
deactivate
