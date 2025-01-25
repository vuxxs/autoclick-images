# autoclick-images

This repository, contains a script designed to automate clicking on images. The script is written in Python and can be configured using environment variables.

## Getting Started

### Prerequisites

To run the script, you need to have [uv](https://docs.astral.sh/uv/getting-started/installation/) installed.

### Running the Script

To execute the script, use the following command:

```sh
uv run ./main.py
```

### Configuration

You can configure the script using the following environment variables:

- `LOOP_DELAY`: Sets the delay between each loop iteration.
- `CONFIDENCE`: Sets the confidence level for image recognition.

Example:

```sh
export LOOP_IDLING_DELAY=30
export CLICK_COOLDOWN=5
export CONFIDENCE=0.8
uv run ./main.py
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## You can find the repository [here](https://github.com/vuxxs/autoclick-images).
