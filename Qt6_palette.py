from PyQt6.QtWidgets import QComboBox
from PyQt6.QtWidgets import QApplication, QStyleFactory
from PyQt6 import QtGui, QtWidgets
from PyQt6.QtGui import QPalette

APP_STYLE = "Fusion"
# Словарь тем
dict_colors = {"Темная": {
    "Window": {"Active": "#2b2b2b", "Inactive": "#2b2b2b", "Disabled": "#1e1e1e"},
    "WindowText": {"Active": "white", "Inactive": "#cccccc", "Disabled": "#666666"},
    "Base": {"Active": "#3c3f41", "Inactive": "#3c3f41", "Disabled": "#2b2b2b"},
    "AlternateBase": {"Active": "#2d2d2d", "Inactive": "#2d2d2d", "Disabled": "#1e1e1e"},
    "ToolTipBase": {"Active": "#4a4a4a", "Inactive": "#4a4a4a", "Disabled": "#333333"},
    "ToolTipText": {"Active": "white", "Inactive": "#cccccc", "Disabled": "#666666"},
    "Text": {"Active": "white", "Inactive": "#cccccc", "Disabled": "#666666"},
    "Button": {"Active": "#3c3f41", "Inactive": "#3c3f41", "Disabled": "#2b2b2b"},
    "ButtonText": {"Active": "white", "Inactive": "#cccccc", "Disabled": "#666666"},
    "BrightText": {"Active": "#ff6666", "Inactive": "#ff6666", "Disabled": "#993333"},
    "Highlight": {"Active": "#3399ff", "Inactive": "#3399ff", "Disabled": "#444444"},
    "HighlightedText": {"Active": "black", "Inactive": "black", "Disabled": "gray"},
    "Link": {"Active": "#3399ff", "Inactive": "#3399ff", "Disabled": "#666666"},
    "LinkVisited": {"Active": "#9966cc", "Inactive": "#9966cc", "Disabled": "#555577"},
    "Shadow": {"Active": "#111111", "Inactive": "#111111", "Disabled": "#000000"},
    "PlaceholderText": {"Active": "#A0A0A0", "Inactive": "#808080", "Disabled": "#606060"},
    "Accent": {"Active": "#FFAA33", "Inactive": "#CC8822", "Disabled": "#885511"},
    "Light": {"Active": "#bbbbbb", "Inactive": "#bbbbbb", "Disabled": "#555555"},
    "Dark": {"Active": "#222222", "Inactive": "#222222", "Disabled": "#111111"},
    "Mid": {"Active": "#444444", "Inactive": "#444444", "Disabled": "#222222"},
    "Midlight": {"Active": "#666666", "Inactive": "#666666", "Disabled": "#333333"}
},
    "Светлая": {
        "Window": {"Active": "white", "Inactive": "#f0f0f0", "Disabled": "#e0e0e0"},
        "WindowText": {"Active": "black", "Inactive": "#333333", "Disabled": "#999999"},
        "Base": {"Active": "white", "Inactive": "#f9f9f9", "Disabled": "#f0f0f0"},
        "AlternateBase": {"Active": "#f5f5f5", "Inactive": "#f5f5f5", "Disabled": "#e0e0e0"},
        "ToolTipBase": {"Active": "#ffffe1", "Inactive": "#ffffe1", "Disabled": "#f0f0c0"},
        "ToolTipText": {"Active": "black", "Inactive": "#333333", "Disabled": "#999999"},
        "Text": {"Active": "black", "Inactive": "#333333", "Disabled": "#999999"},
        "Button": {"Active": "lightgray", "Inactive": "#dcdcdc", "Disabled": "#cccccc"},
        "ButtonText": {"Active": "black", "Inactive": "#333333", "Disabled": "#999999"},
        "BrightText": {"Active": "red", "Inactive": "red", "Disabled": "#aa0000"},
        "Highlight": {"Active": "#0078d7", "Inactive": "#0078d7", "Disabled": "#cccccc"},
        "HighlightedText": {"Active": "white", "Inactive": "white", "Disabled": "gray"},
        "Link": {"Active": "blue", "Inactive": "blue", "Disabled": "#6666aa"},
        "LinkVisited": {"Active": "purple", "Inactive": "purple", "Disabled": "#996699"},
        "Shadow": {"Active": "#666666", "Inactive": "#666666", "Disabled": "#999999"},
        "PlaceholderText": {"Active": "#808080", "Inactive": "#A0A0A0", "Disabled": "#C0C0C0"},
        "Accent": {"Active": "#FF8800", "Inactive": "#CC7000", "Disabled": "#AA5500"},
        "Light": {"Active": "#eeeeee", "Inactive": "#eeeeee", "Disabled": "#cccccc"},
        "Dark": {"Active": "#444444", "Inactive": "#444444", "Disabled": "#222222"},
        "Mid": {"Active": "#888888", "Inactive": "#888888", "Disabled": "#666666"},
        "Midlight": {"Active": "#aaaaaa", "Inactive": "#aaaaaa", "Disabled": "#888888"}
    },
    "Зеленая": {
        "Window": {"Active": "#e9f6ec", "Inactive": "#e9f6ec", "Disabled": "#d8e8da"},
        "WindowText": {"Active": "#0f2414", "Inactive": "#335544", "Disabled": "#779988"},
        "Base": {"Active": "white", "Inactive": "#f4fbf6", "Disabled": "#e0eee4"},
        "AlternateBase": {"Active": "#eef8f1", "Inactive": "#eef8f1", "Disabled": "#d6e4da"},
        "ToolTipBase": {"Active": "#eef8f1", "Inactive": "#eef8f1", "Disabled": "#d6e4da"},
        "ToolTipText": {"Active": "#0f2414", "Inactive": "#335544", "Disabled": "#779988"},
        "Text": {"Active": "#0f2414", "Inactive": "#335544", "Disabled": "#779988"},
        "Button": {"Active": "#d8f0df", "Inactive": "#d8f0df", "Disabled": "#c0d8c7"},
        "ButtonText": {"Active": "#0f2414", "Inactive": "#335544", "Disabled": "#779988"},
        "BrightText": {"Active": "#ff3333", "Inactive": "#ff3333", "Disabled": "#aa2222"},
        "Highlight": {"Active": "#43A047", "Inactive": "#2E7D32", "Disabled": "#A5D6A7"},
        "HighlightedText": {"Active": "white", "Inactive": "white", "Disabled": "#dddddd"},
        "Link": {"Active": "#43A047", "Inactive": "#2E7D32", "Disabled": "#A5D6A7"},
        "LinkVisited": {"Active": "#6A1B9A", "Inactive": "#6A1B9A", "Disabled": "#A0A0C0"},
        "Shadow": {"Active": "#666666", "Inactive": "#666666", "Disabled": "#999999"},
        "PlaceholderText": {"Active": "#607060", "Inactive": "#90A090", "Disabled": "#B0C0B0"},
        "Accent": {"Active": "#43A047", "Inactive": "#2E7D32", "Disabled": "#A5D6A7"},
        "Light": {"Active": "#e0f5e5", "Inactive": "#e0f5e5", "Disabled": "#c0d8c7"},
        "Dark": {"Active": "#2a3d2d", "Inactive": "#2a3d2d", "Disabled": "#1a261c"},
        "Mid": {"Active": "#4a6a4d", "Inactive": "#4a6a4d", "Disabled": "#2f402f"},
        "Midlight": {"Active": "#7a9a7d", "Inactive": "#7a9a7d", "Disabled": "#5a705a"}
    },
    "Голубая": {
        "Window": {"Active": "#e8f1fb", "Inactive": "#e8f1fb", "Disabled": "#d0d8e0"},
        "WindowText": {"Active": "#0d1a26", "Inactive": "#334455", "Disabled": "#778899"},
        "Base": {"Active": "white", "Inactive": "#f5f9ff", "Disabled": "#e0e6ee"},
        "AlternateBase": {"Active": "#f0f6ff", "Inactive": "#f0f6ff", "Disabled": "#d8e0ea"},
        "ToolTipBase": {"Active": "#f0f6ff", "Inactive": "#f0f6ff", "Disabled": "#d8e0ea"},
        "ToolTipText": {"Active": "#0d1a26", "Inactive": "#334455", "Disabled": "#778899"},
        "Text": {"Active": "#0d1a26", "Inactive": "#334455", "Disabled": "#778899"},
        "Button": {"Active": "#d9e8ff", "Inactive": "#d9e8ff", "Disabled": "#c0ccdd"},
        "ButtonText": {"Active": "#0d1a26", "Inactive": "#334455", "Disabled": "#778899"},
        "BrightText": {"Active": "#ff3333", "Inactive": "#ff3333", "Disabled": "#aa2222"},
        "Highlight": {"Active": "#1E88E5", "Inactive": "#1565C0", "Disabled": "#90A4AE"},
        "HighlightedText": {"Active": "white", "Inactive": "white", "Disabled": "#dddddd"},
        "Link": {"Active": "#1E88E5", "Inactive": "#1565C0", "Disabled": "#90A4AE"},
        "LinkVisited": {"Active": "#6A1B9A", "Inactive": "#6A1B9A", "Disabled": "#A0A0C0"},
        "Shadow": {"Active": "#666666", "Inactive": "#666666", "Disabled": "#999999"},
        "PlaceholderText": {"Active": "#607080", "Inactive": "#90A0B0", "Disabled": "#B0B8C0"},
        "Accent": {"Active": "#1E88E5", "Inactive": "#1565C0", "Disabled": "#90A4AE"},
        "Light": {"Active": "#e0efff", "Inactive": "#e0efff", "Disabled": "#c0d0e0"},
        "Dark": {"Active": "#2a3b4d", "Inactive": "#2a3b4d", "Disabled": "#1a222d"},
        "Mid": {"Active": "#4a5a6d", "Inactive": "#4a5a6d", "Disabled": "#2f3a45"},
        "Midlight": {"Active": "#7a8aa0", "Inactive": "#7a8aa0", "Disabled": "#5a6675"}
    },
    "Пурпурная": {
        "Window": {"Active": "#f4e9f8", "Inactive": "#f4e9f8", "Disabled": "#e6d8ea"},
        "WindowText": {"Active": "#1f0f26", "Inactive": "#443355", "Disabled": "#887799"},
        "Base": {"Active": "white", "Inactive": "#fbf4ff", "Disabled": "#eee0f2"},
        "AlternateBase": {"Active": "#f7effc", "Inactive": "#f7effc", "Disabled": "#e3d6e8"},
        "ToolTipBase": {"Active": "#f7effc", "Inactive": "#f7effc", "Disabled": "#e3d6e8"},
        "ToolTipText": {"Active": "#1f0f26", "Inactive": "#443355", "Disabled": "#887799"},
        "Text": {"Active": "#1f0f26", "Inactive": "#443355", "Disabled": "#887799"},
        "Button": {"Active": "#ead8f0", "Inactive": "#ead8f0", "Disabled": "#d4c2d8"},
        "ButtonText": {"Active": "#1f0f26", "Inactive": "#443355", "Disabled": "#887799"},
        "BrightText": {"Active": "#ff3333", "Inactive": "#ff3333", "Disabled": "#aa2222"},
        "Highlight": {"Active": "#8E24AA", "Inactive": "#6A1B9A", "Disabled": "#CE93D8"},
        "HighlightedText": {"Active": "white", "Inactive": "white", "Disabled": "#dddddd"},
        "Link": {"Active": "#8E24AA", "Inactive": "#6A1B9A", "Disabled": "#CE93D8"},
        "LinkVisited": {"Active": "#4A148C", "Inactive": "#4A148C", "Disabled": "#A080C0"},
        "Shadow": {"Active": "#666666", "Inactive": "#666666", "Disabled": "#999999"},
        "PlaceholderText": {"Active": "#705a70", "Inactive": "#A090A0", "Disabled": "#C0B0C0"},
        "Accent": {"Active": "#8E24AA", "Inactive": "#6A1B9A", "Disabled": "#CE93D8"},
        "Light": {"Active": "#f0e0f5", "Inactive": "#f0e0f5", "Disabled": "#d8c8dd"},
        "Dark": {"Active": "#3a2a3d", "Inactive": "#3a2a3d", "Disabled": "#241a26"},
        "Mid": {"Active": "#5a4a5d", "Inactive": "#5a4a5d", "Disabled": "#3a2f3d"},
        "Midlight": {"Active": "#8a7a8d", "Inactive": "#8a7a8d", "Disabled": "#6a5a6d"}
    },
    "Розовая": {
        "Window": {"Active": "#fde8f1", "Inactive": "#fde8f1", "Disabled": "#f2d6e0"},
        "WindowText": {"Active": "#2a0f1f", "Inactive": "#553344", "Disabled": "#997788"},
        "Base": {"Active": "white", "Inactive": "#fff5fa", "Disabled": "#f2e0e8"},
        "AlternateBase": {"Active": "#fdeff6", "Inactive": "#fdeff6", "Disabled": "#ead6e0"},
        "ToolTipBase": {"Active": "#fdeff6", "Inactive": "#fdeff6", "Disabled": "#ead6e0"},
        "ToolTipText": {"Active": "#2a0f1f", "Inactive": "#553344", "Disabled": "#997788"},
        "Text": {"Active": "#2a0f1f", "Inactive": "#553344", "Disabled": "#997788"},
        "Button": {"Active": "#f5d8e4", "Inactive": "#f5d8e4", "Disabled": "#e0c2cc"},
        "ButtonText": {"Active": "#2a0f1f", "Inactive": "#553344", "Disabled": "#997788"},
        "BrightText": {"Active": "#ff3333", "Inactive": "#ff3333", "Disabled": "#aa2222"},
        "Highlight": {"Active": "#EC407A", "Inactive": "#D81B60", "Disabled": "#F8BBD0"},
        "HighlightedText": {"Active": "white", "Inactive": "white", "Disabled": "#dddddd"},
        "Link": {"Active": "#EC407A", "Inactive": "#D81B60", "Disabled": "#F8BBD0"},
        "LinkVisited": {"Active": "#AD1457", "Inactive": "#AD1457", "Disabled": "#C090A0"},
        "Shadow": {"Active": "#666666", "Inactive": "#666666", "Disabled": "#999999"},
        "PlaceholderText": {"Active": "#705060", "Inactive": "#A08090", "Disabled": "#C0A8B0"},
        "Accent": {"Active": "#EC407A", "Inactive": "#D81B60", "Disabled": "#F8BBD0"},
        "Light": {"Active": "#f7e0ea", "Inactive": "#f7e0ea", "Disabled": "#e0c8d2"},
        "Dark": {"Active": "#3d2a33", "Inactive": "#3d2a33", "Disabled": "#241a22"},
        "Mid": {"Active": "#6a4a5a", "Inactive": "#6a4a5a", "Disabled": "#3f2f3a"},
        "Midlight": {"Active": "#9a7a8a", "Inactive": "#9a7a8a", "Disabled": "#6a5a66"}
    },
    "Красная": {
        "Window": {"Active": "#fdeaea", "Inactive": "#fdeaea", "Disabled": "#f2dcdc"},
        "WindowText": {"Active": "#260f0f", "Inactive": "#553333", "Disabled": "#997777"},
        "Base": {"Active": "white", "Inactive": "#fff5f5", "Disabled": "#f2e0e0"},
        "AlternateBase": {"Active": "#fceeee", "Inactive": "#fceeee", "Disabled": "#ead6d6"},
        "ToolTipBase": {"Active": "#fceeee", "Inactive": "#fceeee", "Disabled": "#ead6d6"},
        "ToolTipText": {"Active": "#260f0f", "Inactive": "#553333", "Disabled": "#997777"},
        "Text": {"Active": "#260f0f", "Inactive": "#553333", "Disabled": "#997777"},
        "Button": {"Active": "#f5d8d8", "Inactive": "#f5d8d8", "Disabled": "#e0c2c2"},
        "ButtonText": {"Active": "#260f0f", "Inactive": "#553333", "Disabled": "#997777"},
        "BrightText": {"Active": "#ff0000", "Inactive": "#ff0000", "Disabled": "#aa0000"},
        "Highlight": {"Active": "#E53935", "Inactive": "#C62828", "Disabled": "#EF9A9A"},
        "HighlightedText": {"Active": "white", "Inactive": "white", "Disabled": "#dddddd"},
        "Link": {"Active": "#E53935", "Inactive": "#C62828", "Disabled": "#EF9A9A"},
        "LinkVisited": {"Active": "#8E0000", "Inactive": "#8E0000", "Disabled": "#B08080"},
        "Shadow": {"Active": "#666666", "Inactive": "#666666", "Disabled": "#999999"},
        "PlaceholderText": {"Active": "#705050", "Inactive": "#A08080", "Disabled": "#C0A8A8"},
        "Accent": {"Active": "#E53935", "Inactive": "#C62828", "Disabled": "#EF9A9A"},
        "Light": {"Active": "#f7e0e0", "Inactive": "#f7e0e0", "Disabled": "#e0c8c8"},
        "Dark": {"Active": "#3d2a2a", "Inactive": "#3d2a2a", "Disabled": "#241a1a"},
        "Mid": {"Active": "#6a4a4a", "Inactive": "#6a4a4a", "Disabled": "#3f2f2f"},
        "Midlight": {"Active": "#9a7a7a", "Inactive": "#9a7a7a", "Disabled": "#6a5a5a"}
    },
    "Бирюзовая": {
        "Window": {"Active": "#e6f7f7", "Inactive": "#e6f7f7", "Disabled": "#d4eaea"},
        "WindowText": {"Active": "#0f2424", "Inactive": "#335555", "Disabled": "#779999"},
        "Base": {"Active": "white", "Inactive": "#f4fbfb", "Disabled": "#e0eeee"},
        "AlternateBase": {"Active": "#eef8f8", "Inactive": "#eef8f8", "Disabled": "#d6e4e4"},
        "ToolTipBase": {"Active": "#eef8f8", "Inactive": "#eef8f8", "Disabled": "#d6e4e4"},
        "ToolTipText": {"Active": "#0f2424", "Inactive": "#335555", "Disabled": "#779999"},
        "Text": {"Active": "#0f2424", "Inactive": "#335555", "Disabled": "#779999"},
        "Button": {"Active": "#d8f0f0", "Inactive": "#d8f0f0", "Disabled": "#c0d8d8"},
        "ButtonText": {"Active": "#0f2424", "Inactive": "#335555", "Disabled": "#779999"},
        "BrightText": {"Active": "#ff3333", "Inactive": "#ff3333", "Disabled": "#aa2222"},
        "Highlight": {"Active": "#26A69A", "Inactive": "#00897B", "Disabled": "#80CBC4"},
        "HighlightedText": {"Active": "white", "Inactive": "white", "Disabled": "#dddddd"},
        "Link": {"Active": "#26A69A", "Inactive": "#00897B", "Disabled": "#80CBC4"},
        "LinkVisited": {"Active": "#004D40", "Inactive": "#004D40", "Disabled": "#80A0A0"},
        "Shadow": {"Active": "#666666", "Inactive": "#666666", "Disabled": "#999999"},
        "PlaceholderText": {"Active": "#506060", "Inactive": "#809090", "Disabled": "#A8B8B8"},
        "Accent": {"Active": "#26A69A", "Inactive": "#00897B", "Disabled": "#80CBC4"},
        "Light": {"Active": "#e0f5f5", "Inactive": "#e0f5f5", "Disabled": "#c0d8d8"},
        "Dark": {"Active": "#2a3d3d", "Inactive": "#2a3d3d", "Disabled": "#1a2626"},
        "Mid": {"Active": "#4a6a6a", "Inactive": "#4a6a6a", "Disabled": "#2f4040"},
        "Midlight": {"Active": "#7a9a9a", "Inactive": "#7a9a9a", "Disabled": "#5a7070"}
    },
    "Янтарная": {
        "Window": {"Active": "#fff4e0", "Inactive": "#fff4e0", "Disabled": "#f2e6d0"},
        "WindowText": {"Active": "#261f0f", "Inactive": "#554433", "Disabled": "#998877"},
        "Base": {"Active": "white", "Inactive": "#fff9f0", "Disabled": "#f2e8d8"},
        "AlternateBase": {"Active": "#fff2e0", "Inactive": "#fff2e0", "Disabled": "#eadcc8"},
        "ToolTipBase": {"Active": "#fff2e0", "Inactive": "#fff2e0", "Disabled": "#eadcc8"},
        "ToolTipText": {"Active": "#261f0f", "Inactive": "#554433", "Disabled": "#998877"},
        "Text": {"Active": "#261f0f", "Inactive": "#554433", "Disabled": "#998877"},
        "Button": {"Active": "#f5e2c8", "Inactive": "#f5e2c8", "Disabled": "#e0d0b8"},
        "ButtonText": {"Active": "#261f0f", "Inactive": "#554433", "Disabled": "#998877"},
        "BrightText": {"Active": "#ff3333", "Inactive": "#ff3333", "Disabled": "#aa2222"},
        "Highlight": {"Active": "#FFB300", "Inactive": "#FFA000", "Disabled": "#FFE082"},
        "HighlightedText": {"Active": "black", "Inactive": "black", "Disabled": "#555555"},
        "Link": {"Active": "#FFB300", "Inactive": "#FFA000", "Disabled": "#FFE082"},
        "LinkVisited": {"Active": "#FF6F00", "Inactive": "#FF6F00", "Disabled": "#D0A060"},
        "Shadow": {"Active": "#666666", "Inactive": "#666666", "Disabled": "#999999"},
        "PlaceholderText": {"Active": "#706050", "Inactive": "#A09080", "Disabled": "#C0B0A0"},
        "Accent": {"Active": "#FFB300", "Inactive": "#FFA000", "Disabled": "#FFE082"},
        "Light": {"Active": "#fff0d0", "Inactive": "#fff0d0", "Disabled": "#e8d8c0"},
        "Dark": {"Active": "#3d2f1a", "Inactive": "#3d2f1a", "Disabled": "#241c10"},
        "Mid": {"Active": "#6a5a40", "Inactive": "#6a5a40", "Disabled": "#3f3a28"},
        "Midlight": {"Active": "#9a8a70", "Inactive": "#9a8a70", "Disabled": "#6a5a40"}
    },
    "Голубая 2": {
        "Window": {"Active": "#007FFF", "Inactive": "#0066CC", "Disabled": "#003366"},
        "WindowText": {"Active": "white", "Inactive": "#E0E0E0", "Disabled": "#808080"},
        "Base": {"Active": "#F0F8FF", "Inactive": "#F0F8FF", "Disabled": "#D0D0D0"},
        "AlternateBase": {"Active": "#E1F5FE", "Inactive": "#E1F5FE", "Disabled": "#B3E5FC"},
        "ToolTipBase": {"Active": "#004080", "Inactive": "#004080", "Disabled": "#002040"},
        "ToolTipText": {"Active": "white", "Inactive": "white", "Disabled": "#A0A0A0"},
        "Text": {"Active": "#003366", "Inactive": "#333333", "Disabled": "#757575"},
        "Button": {"Active": "#007FFF", "Inactive": "#007FFF", "Disabled": "#B0C4DE"},
        "ButtonText": {"Active": "white", "Inactive": "white", "Disabled": "#D1D1D1"},
        "BrightText": {"Active": "#FFFFFF", "Inactive": "#FFFFFF", "Disabled": "#B0B0B0"},
        "Highlight": {"Active": "#FFD700", "Inactive": "#FFCC00", "Disabled": "#404040"},
        "HighlightedText": {"Active": "black", "Inactive": "black", "Disabled": "white"},
        "Link": {"Active": "#00BFFF", "Inactive": "#00BFFF", "Disabled": "#4682B4"},
        "LinkVisited": {"Active": "#8A2BE2", "Inactive": "#8A2BE2", "Disabled": "#4B0082"},
        "Shadow": {"Active": "#002244", "Inactive": "#002244", "Disabled": "#000000"},
        "PlaceholderText": {"Active": "#80BFFF", "Inactive": "#6699CC", "Disabled": "#4D6680"},
        "Accent": {"Active": "#FF6F00", "Inactive": "#FF6F00", "Disabled": "#8B4513"},
        "Light": {"Active": "#CCE5FF", "Inactive": "#CCE5FF", "Disabled": "#667788"},
        "Dark": {"Active": "#004080", "Inactive": "#004080", "Disabled": "#001122"},
        "Mid": {"Active": "#005BB7", "Inactive": "#005BB7", "Disabled": "#002D5B"},
        "Midlight": {"Active": "#3399FF", "Inactive": "#3399FF", "Disabled": "#1A4D80"}
    },
    "Пастельная": {
        "Window": {"Active": "#FEF7FF", "Inactive": "#FEF7FF", "Disabled": "#F3F3F3"},
        "WindowText": {"Active": "#1D1B20", "Inactive": "#1D1B20", "Disabled": "#938F99"},
        "Base": {"Active": "#F7F2FA", "Inactive": "#F7F2FA", "Disabled": "#E6E1E5"},
        "AlternateBase": {"Active": "#F3EDF7", "Inactive": "#F3EDF7", "Disabled": "#DED8E1"},
        "ToolTipBase": {"Active": "#313033", "Inactive": "#313033", "Disabled": "#1C1B1F"},
        "ToolTipText": {"Active": "#F4EFF4", "Inactive": "#F4EFF4", "Disabled": "#938F99"},
        "Text": {"Active": "#1C1B1F", "Inactive": "#1C1B1F", "Disabled": "#938F99"},
        "Button": {"Active": "#EADDFF", "Inactive": "#EADDFF", "Disabled": "#E6E1E5"},
        "ButtonText": {"Active": "#21005D", "Inactive": "#21005D", "Disabled": "#938F99"},
        "BrightText": {"Active": "#FFFFFF", "Inactive": "#FFFFFF", "Disabled": "#B0B0B0"},
        "Highlight": {"Active": "#D0BCFF", "Inactive": "#D0BCFF", "Disabled": "#49454F"},
        "HighlightedText": {"Active": "#381E72", "Inactive": "#381E72", "Disabled": "#CAC4D0"},
        "Link": {"Active": "#6750A4", "Inactive": "#6750A4", "Disabled": "#938F99"},
        "LinkVisited": {"Active": "#21005D", "Inactive": "#21005D", "Disabled": "#49454F"},
        "Shadow": {"Active": "#000000", "Inactive": "#000000", "Disabled": "#000000"},
        "PlaceholderText": {"Active": "#49454F", "Inactive": "#49454F", "Disabled": "#938F99"},
        "Accent": {"Active": "#7D5260", "Inactive": "#7D5260", "Disabled": "#49454F"},
        "Light": {"Active": "#FFFFFF", "Inactive": "#FFFFFF", "Disabled": "#E6E1E5"},
        "Dark": {"Active": "#CAC4D0", "Inactive": "#CAC4D0", "Disabled": "#938F99"},
        "Mid": {"Active": "#938F99", "Inactive": "#938F99", "Disabled": "#49454F"},
        "Midlight": {"Active": "#E6E1E5", "Inactive": "#E6E1E5", "Disabled": "#CAC4D0"}
    },
    "Арктическая, холодная": {
        "Window": {"Active": "#2E3440", "Inactive": "#2E3440", "Disabled": "#242933"},
        "WindowText": {"Active": "#D8DEE9", "Inactive": "#999999", "Disabled": "#4C566A"},
        "Base": {"Active": "#3B4252", "Inactive": "#3B4252", "Disabled": "#2E3440"},
        "AlternateBase": {"Active": "#434C5E", "Inactive": "#434C5E", "Disabled": "#3B4252"},
        "ToolTipBase": {"Active": "#4C566A", "Inactive": "#4C566A", "Disabled": "#3B4252"},
        "ToolTipText": {"Active": "#ECEFF4", "Inactive": "#D8DEE9", "Disabled": "#4C566A"},
        "Text": {"Active": "#ECEFF4", "Inactive": "#D8DEE9", "Disabled": "#4C566A"},
        "Button": {"Active": "#434C5E", "Inactive": "#434C5E", "Disabled": "#3B4252"},
        "ButtonText": {"Active": "#D8DEE9", "Inactive": "#D8DEE9", "Disabled": "#4C566A"},
        "BrightText": {"Active": "#88C0D0", "Inactive": "#88C0D0", "Disabled": "#5E81AC"},
        "Highlight": {"Active": "#88C0D0", "Inactive": "#81A1C1", "Disabled": "#4C566A"},
        "HighlightedText": {"Active": "#2E3440", "Inactive": "#2E3440", "Disabled": "#D8DEE9"},
        "Link": {"Active": "#81A1C1", "Inactive": "#81A1C1", "Disabled": "#5E81AC"},
        "LinkVisited": {"Active": "#B48EAD", "Inactive": "#B48EAD", "Disabled": "#4C566A"},
        "Shadow": {"Active": "#1A2026", "Inactive": "#1A2026", "Disabled": "#000000"},
        "PlaceholderText": {"Active": "#4C566A", "Inactive": "#434C5E", "Disabled": "#3B4252"},
        "Accent": {"Active": "#A3BE8C", "Inactive": "#8FBCBB", "Disabled": "#4C566A"},
        "Light": {"Active": "#4C566A", "Inactive": "#4C566A", "Disabled": "#2E3440"},
        "Dark": {"Active": "#242933", "Inactive": "#242933", "Disabled": "#1A2026"},
        "Mid": {"Active": "#3B4252", "Inactive": "#3B4252", "Disabled": "#2E3440"},
        "Midlight": {"Active": "#434C5E", "Inactive": "#434C5E", "Disabled": "#3B4252"}
    },
    "Контрастная, фиолетово‑неоновая)": {
        "Window": {"Active": "#282A36", "Inactive": "#282A36", "Disabled": "#1E1F29"},
        "WindowText": {"Active": "#F8F8F2", "Inactive": "#6272A4", "Disabled": "#44475A"},
        "Base": {"Active": "#44475A", "Inactive": "#44475A", "Disabled": "#282A36"},
        "AlternateBase": {"Active": "#343746", "Inactive": "#343746", "Disabled": "#282A36"},
        "ToolTipBase": {"Active": "#6272A4", "Inactive": "#6272A4", "Disabled": "#44475A"},
        "ToolTipText": {"Active": "#F8F8F2", "Inactive": "#F8F8F2", "Disabled": "#6272A4"},
        "Text": {"Active": "#F8F8F2", "Inactive": "#6272A4", "Disabled": "#44475A"},
        "Button": {"Active": "#6272A4", "Inactive": "#6272A4", "Disabled": "#44475A"},
        "ButtonText": {"Active": "#F8F8F2", "Inactive": "#F8F8F2", "Disabled": "#44475A"},
        "BrightText": {"Active": "#FF79C6", "Inactive": "#FF79C6", "Disabled": "#BD93F9"},
        "Highlight": {"Active": "#BD93F9", "Inactive": "#BD93F9", "Disabled": "#44475A"},
        "HighlightedText": {"Active": "#282A36", "Inactive": "#282A36", "Disabled": "#F8F8F2"},
        "Link": {"Active": "#8BE9FD", "Inactive": "#8BE9FD", "Disabled": "#6272A4"},
        "LinkVisited": {"Active": "#FF79C6", "Inactive": "#FF79C6", "Disabled": "#BD93F9"},
        "Shadow": {"Active": "#000000", "Inactive": "#000000", "Disabled": "#000000"},
        "PlaceholderText": {"Active": "#6272A4", "Inactive": "#6272A4", "Disabled": "#44475A"},
        "Accent": {"Active": "#50FA7B", "Inactive": "#F1FA8C", "Disabled": "#44475A"},
        "Light": {"Active": "#6272A4", "Inactive": "#6272A4", "Disabled": "#44475A"},
        "Dark": {"Active": "#191A21", "Inactive": "#191A21", "Disabled": "#000000"},
        "Mid": {"Active": "#282A36", "Inactive": "#282A36", "Disabled": "#191A21"},
        "Midlight": {"Active": "#44475A", "Inactive": "#44475A", "Disabled": "#282A36"}
    },
    "Solarized Dark - классическая «дизайнерская»": {
        "Window": {"Active": "#002b36", "Inactive": "#002b36", "Disabled": "#073642"},
        "WindowText": {"Active": "#839496", "Inactive": "#586e75", "Disabled": "#586e75"},
        "Base": {"Active": "#073642", "Inactive": "#073642", "Disabled": "#002b36"},
        "AlternateBase": {"Active": "#00212b", "Inactive": "#00212b", "Disabled": "#001a21"},
        "ToolTipBase": {"Active": "#586e75", "Inactive": "#586e75", "Disabled": "#073642"},
        "ToolTipText": {"Active": "#93a1a1", "Inactive": "#93a1a1", "Disabled": "#586e75"},
        "Text": {"Active": "#93a1a1", "Inactive": "#839496", "Disabled": "#586e75"},
        "Button": {"Active": "#073642", "Inactive": "#073642", "Disabled": "#002b36"},
        "ButtonText": {"Active": "#839496", "Inactive": "#839496", "Disabled": "#586e75"},
        "BrightText": {"Active": "#cb4b16", "Inactive": "#cb4b16", "Disabled": "#859900"},
        "Highlight": {"Active": "#268bd2", "Inactive": "#268bd2", "Disabled": "#073642"},
        "HighlightedText": {"Active": "#eee8d5", "Inactive": "#eee8d5", "Disabled": "#93a1a1"},
        "Link": {"Active": "#268bd2", "Inactive": "#268bd2", "Disabled": "#2aa198"},
        "LinkVisited": {"Active": "#6c71c4", "Inactive": "#6c71c4", "Disabled": "#586e75"},
        "Shadow": {"Active": "#001e26", "Inactive": "#001e26", "Disabled": "#000000"},
        "PlaceholderText": {"Active": "#586e75", "Inactive": "#586e75", "Disabled": "#073642"},
        "Accent": {"Active": "#b58900", "Inactive": "#b58900", "Disabled": "#073642"},
        "Light": {"Active": "#586e75", "Inactive": "#586e75", "Disabled": "#073642"},
        "Dark": {"Active": "#001e26", "Inactive": "#001e26", "Disabled": "#000000"},
        "Mid": {"Active": "#073642", "Inactive": "#073642", "Disabled": "#002b36"},
        "Midlight": {"Active": "#586e75", "Inactive": "#586e75", "Disabled": "#073642"}
    },
    "Gruvbox - теплая, «крафтовая»": {
        "Window": {"Active": "#282828", "Inactive": "#282828", "Disabled": "#1d2021"},
        "WindowText": {"Active": "#ebdbb2", "Inactive": "#a89984", "Disabled": "#7c6f64"},
        "Base": {"Active": "#3c3836", "Inactive": "#3c3836", "Disabled": "#282828"},
        "AlternateBase": {"Active": "#32302f", "Inactive": "#32302f", "Disabled": "#282828"},
        "ToolTipBase": {"Active": "#1d2021", "Inactive": "#1d2021", "Disabled": "#1d2021"},
        "ToolTipText": {"Active": "#ebdbb2", "Inactive": "#ebdbb2", "Disabled": "#a89984"},
        "Text": {"Active": "#ebdbb2", "Inactive": "#d5c4a1", "Disabled": "#7c6f64"},
        "Button": {"Active": "#504945", "Inactive": "#504945", "Disabled": "#3c3836"},
        "ButtonText": {"Active": "#ebdbb2", "Inactive": "#ebdbb2", "Disabled": "#7c6f64"},
        "BrightText": {"Active": "#fb4934", "Inactive": "#fb4934", "Disabled": "#9d0006"},
        "Highlight": {"Active": "#fabd2f", "Inactive": "#fabd2f", "Disabled": "#504945"},
        "HighlightedText": {"Active": "#282828", "Inactive": "#282828", "Disabled": "#7c6f64"},
        "Link": {"Active": "#83a598", "Inactive": "#83a598", "Disabled": "#458588"},
        "LinkVisited": {"Active": "#d3869b", "Inactive": "#d3869b", "Disabled": "#b16286"},
        "Shadow": {"Active": "#1a1a1a", "Inactive": "#1a1a1a", "Disabled": "#000000"},
        "PlaceholderText": {"Active": "#928374", "Inactive": "#7c6f64", "Disabled": "#504945"},
        "Accent": {"Active": "#fe8019", "Inactive": "#fe8019", "Disabled": "#af3a03"},
        "Light": {"Active": "#7c6f64", "Inactive": "#7c6f64", "Disabled": "#3c3836"},
        "Dark": {"Active": "#1d2021", "Inactive": "#1d2021", "Disabled": "#000000"},
        "Mid": {"Active": "#504945", "Inactive": "#504945", "Disabled": "#3c3836"},
        "Midlight": {"Active": "#665c54", "Inactive": "#665c54", "Disabled": "#504945"}
    },
    "One Dark - профессиональная темно-серая": {
        "Window": {"Active": "#282c34", "Inactive": "#282c34", "Disabled": "#21252b"},
        "WindowText": {"Active": "#abb2bf", "Inactive": "#828997", "Disabled": "#5c6370"},
        "Base": {"Active": "#21252b", "Inactive": "#21252b", "Disabled": "#181a1f"},
        "AlternateBase": {"Active": "#2c313a", "Inactive": "#2c313a", "Disabled": "#21252b"},
        "ToolTipBase": {"Active": "#3e4452", "Inactive": "#3e4452", "Disabled": "#21252b"},
        "ToolTipText": {"Active": "#abb2bf", "Inactive": "#abb2bf", "Disabled": "#5c6370"},
        "Text": {"Active": "#abb2bf", "Inactive": "#abb2bf", "Disabled": "#5c6370"},
        "Button": {"Active": "#353b45", "Inactive": "#353b45", "Disabled": "#282c34"},
        "ButtonText": {"Active": "#abb2bf", "Inactive": "#abb2bf", "Disabled": "#5c6370"},
        "BrightText": {"Active": "#e06c75", "Inactive": "#e06c75", "Disabled": "#be5046"},
        "Highlight": {"Active": "#61afef", "Inactive": "#61afef", "Disabled": "#3e4451"},
        "HighlightedText": {"Active": "#282c34", "Inactive": "#282c34", "Disabled": "#abb2bf"},
        "Link": {"Active": "#56b6c2", "Inactive": "#56b6c2", "Disabled": "#4b5263"},
        "LinkVisited": {"Active": "#c678dd", "Inactive": "#c678dd", "Disabled": "#5c6370"},
        "Shadow": {"Active": "#181a1f", "Inactive": "#181a1f", "Disabled": "#000000"},
        "PlaceholderText": {"Active": "#5c6370", "Inactive": "#4b5263", "Disabled": "#3e4452"},
        "Accent": {"Active": "#98c379", "Inactive": "#98c379", "Disabled": "#5c6370"},
        "Light": {"Active": "#4b5263", "Inactive": "#4b5263", "Disabled": "#21252b"},
        "Dark": {"Active": "#181a1f", "Inactive": "#181a1f", "Disabled": "#000000"},
        "Mid": {"Active": "#3e4452", "Inactive": "#3e4452", "Disabled": "#21252b"},
        "Midlight": {"Active": "#4b5263", "Inactive": "#4b5263", "Disabled": "#353b45"}
    },
    "Cyberpunk - экстремально контрастная": {
        "Window": {"Active": "#000000", "Inactive": "#000000", "Disabled": "#0d0d0d"},
        "WindowText": {"Active": "#f5f5f5", "Inactive": "#888888", "Disabled": "#444444"},
        "Base": {"Active": "#111111", "Inactive": "#111111", "Disabled": "#000000"},
        "AlternateBase": {"Active": "#1a1a1a", "Inactive": "#1a1a1a", "Disabled": "#0d0d0d"},
        "ToolTipBase": {"Active": "#fcee0a", "Inactive": "#fcee0a", "Disabled": "#777700"},
        "ToolTipText": {"Active": "#000000", "Inactive": "#000000", "Disabled": "#000000"},
        "Text": {"Active": "#00ff9f", "Inactive": "#00b36f", "Disabled": "#00442b"},
        "Button": {"Active": "#fcee0a", "Inactive": "#fcee0a", "Disabled": "#444400"},
        "ButtonText": {"Active": "#000000", "Inactive": "#000000", "Disabled": "#444444"},
        "BrightText": {"Active": "#ff003c", "Inactive": "#ff003c", "Disabled": "#880020"},
        "Highlight": {"Active": "#00f0ff", "Inactive": "#00f0ff", "Disabled": "#005555"},
        "HighlightedText": {"Active": "#000000", "Inactive": "#000000", "Disabled": "#ffffff"},
        "Link": {"Active": "#ff003c", "Inactive": "#ff003c", "Disabled": "#880020"},
        "LinkVisited": {"Active": "#ab00ff", "Inactive": "#ab00ff", "Disabled": "#550088"},
        "Shadow": {"Active": "#000000", "Inactive": "#000000", "Disabled": "#000000"},
        "PlaceholderText": {"Active": "#555555", "Inactive": "#333333", "Disabled": "#222222"},
        "Accent": {"Active": "#fcee0a", "Inactive": "#fcee0a", "Disabled": "#888800"},
        "Light": {"Active": "#333333", "Inactive": "#333333", "Disabled": "#111111"},
        "Dark": {"Active": "#000000", "Inactive": "#000000", "Disabled": "#000000"},
        "Mid": {"Active": "#222222", "Inactive": "#222222", "Disabled": "#111111"},
        "Midlight": {"Active": "#444444", "Inactive": "#444444", "Disabled": "#222222"}
    },
    "Бренд Ferrari": {
        "Window": {"Active": "#1a1a1a", "Inactive": "#1a1a1a", "Disabled": "#121212"},
        "WindowText": {"Active": "white", "Inactive": "#aaaaaa", "Disabled": "#555555"},
        "Base": {"Active": "#2d2d2d", "Inactive": "#2d2d2d", "Disabled": "#1a1a1a"},
        "AlternateBase": {"Active": "#222222", "Inactive": "#222222", "Disabled": "#1a1a1a"},
        "ToolTipBase": {"Active": "#ff2800", "Inactive": "#ff2800", "Disabled": "#991800"},
        "ToolTipText": {"Active": "white", "Inactive": "white", "Disabled": "#cccccc"},
        "Text": {"Active": "white", "Inactive": "#dddddd", "Disabled": "#777777"},
        "Button": {"Active": "#ff2800", "Inactive": "#cc2000", "Disabled": "#551100"},
        "ButtonText": {"Active": "white", "Inactive": "white", "Disabled": "#888888"},
        "BrightText": {"Active": "#fff200", "Inactive": "#fff200", "Disabled": "#999100"},  # Фирменный желтый Scuderia
        "Highlight": {"Active": "#ff2800", "Inactive": "#cc2000", "Disabled": "#444444"},
        "HighlightedText": {"Active": "white", "Inactive": "white", "Disabled": "#bbbbbb"},
        "Link": {"Active": "#fff200", "Inactive": "#fff200", "Disabled": "#999100"},
        "LinkVisited": {"Active": "#cccccc", "Inactive": "#cccccc", "Disabled": "#666666"},
        "Shadow": {"Active": "#000000", "Inactive": "#000000", "Disabled": "#000000"},
        "PlaceholderText": {"Active": "#666666", "Inactive": "#444444", "Disabled": "#333333"},
        "Accent": {"Active": "#fff200", "Inactive": "#ccbc00", "Disabled": "#665e00"},
        "Light": {"Active": "#444444", "Inactive": "#444444", "Disabled": "#222222"},
        "Dark": {"Active": "#0a0a0a", "Inactive": "#0a0a0a", "Disabled": "#000000"},
        "Mid": {"Active": "#2d2d2d", "Inactive": "#2d2d2d", "Disabled": "#1a1a1a"},
        "Midlight": {"Active": "#3d3d3d", "Inactive": "#3d3d3d", "Disabled": "#2d2d2d"}
    },
    "Бренд Moulinex": {
        "Window": {"Active": "#fcfcfc", "Inactive": "#f5f5f5", "Disabled": "#e0e0e0"},
        "WindowText": {"Active": "#333333", "Inactive": "#666666", "Disabled": "#999999"},
        "Base": {"Active": "white", "Inactive": "white", "Disabled": "#f0f0f0"},
        "AlternateBase": {"Active": "#f7f7f7", "Inactive": "#f7f7f7", "Disabled": "#e8e8e8"},
        "ToolTipBase": {"Active": "#333333", "Inactive": "#333333", "Disabled": "#555555"},
        "ToolTipText": {"Active": "white", "Inactive": "white", "Disabled": "#aaaaaa"},
        "Text": {"Active": "#222222", "Inactive": "#444444", "Disabled": "#888888"},
        "Button": {"Active": "#da291c", "Inactive": "#da291c", "Disabled": "#f5b0ab"},  # Рубиновый Moulinex
        "ButtonText": {"Active": "white", "Inactive": "white", "Disabled": "#eeeeee"},
        "BrightText": {"Active": "#da291c", "Inactive": "#da291c", "Disabled": "#aa2016"},
        "Highlight": {"Active": "#da291c", "Inactive": "#c02418", "Disabled": "#cccccc"},
        "HighlightedText": {"Active": "white", "Inactive": "white", "Disabled": "#f0f0f0"},
        "Link": {"Active": "#da291c", "Inactive": "#da291c", "Disabled": "#aa2016"},
        "LinkVisited": {"Active": "#801810", "Inactive": "#801810", "Disabled": "#50100a"},
        "Shadow": {"Active": "#dcdcdc", "Inactive": "#dcdcdc", "Disabled": "#b0b0b0"},
        "PlaceholderText": {"Active": "#999999", "Inactive": "#bbbbbb", "Disabled": "#cccccc"},
        "Accent": {"Active": "#da291c", "Inactive": "#da291c", "Disabled": "#aa2016"},
        "Light": {"Active": "#ffffff", "Inactive": "#ffffff", "Disabled": "#f5f5f5"},
        "Dark": {"Active": "#d1d1d1", "Inactive": "#d1d1d1", "Disabled": "#b0b0b0"},
        "Mid": {"Active": "#e0e0e0", "Inactive": "#e0e0e0", "Disabled": "#c0c0c0"},
        "Midlight": {"Active": "#f0f0f0", "Inactive": "#f0f0f0", "Disabled": "#e0e0e0"}
    },
    "Commodore 64 (Ретро)": {
        "Window": {"Active": "#352879", "Inactive": "#352879", "Disabled": "#20184a"},  # Фирменный темно-синий
        "WindowText": {"Active": "#6c5eb5", "Inactive": "#6c5eb5", "Disabled": "#443b71"},  # Светло-синий текст
        "Base": {"Active": "#352879", "Inactive": "#352879", "Disabled": "#20184a"},
        "AlternateBase": {"Active": "#42348b", "Inactive": "#42348b", "Disabled": "#352879"},
        "ToolTipBase": {"Active": "#000000", "Inactive": "#000000", "Disabled": "#000000"},
        "ToolTipText": {"Active": "#ffffff", "Inactive": "#ffffff", "Disabled": "#959595"},
        "Text": {"Active": "#6c5eb5", "Inactive": "#6c5eb5", "Disabled": "#443b71"},
        "Button": {"Active": "#6c5eb5", "Inactive": "#6c5eb5", "Disabled": "#352879"},
        "ButtonText": {"Active": "#352879", "Inactive": "#352879", "Disabled": "#20184a"},
        "BrightText": {"Active": "#ffffff", "Inactive": "#ffffff", "Disabled": "#adadad"},
        "Highlight": {"Active": "#70a646", "Inactive": "#70a646", "Disabled": "#3e5b27"},  # Классический зеленый C64
        "HighlightedText": {"Active": "#ffffff", "Inactive": "#ffffff", "Disabled": "#959595"},
        "Link": {"Active": "#588d43", "Inactive": "#588d43", "Disabled": "#355229"},
        "LinkVisited": {"Active": "#b23f3f", "Inactive": "#b23f3f", "Disabled": "#6d2727"},
        "Shadow": {"Active": "#000000", "Inactive": "#000000", "Disabled": "#000000"},
        "PlaceholderText": {"Active": "#443b71", "Inactive": "#443b71", "Disabled": "#352879"},
        "Accent": {"Active": "#9a6759", "Inactive": "#9a6759", "Disabled": "#5e3f37"},  # Коричневый оттенок палитры
        "Light": {"Active": "#959595", "Inactive": "#959595", "Disabled": "#686868"},
        "Dark": {"Active": "#000000", "Inactive": "#000000", "Disabled": "#000000"},
        "Mid": {"Active": "#686868", "Inactive": "#686868", "Disabled": "#333333"},
        "Midlight": {"Active": "#adadad", "Inactive": "#adadad", "Disabled": "#959595"}
    },
    "IBM 3270 (Зеленый терминал)": {
        "Window": {"Active": "#000000", "Inactive": "#000000", "Disabled": "#050505"},
        "WindowText": {"Active": "#00ff33", "Inactive": "#00cc22", "Disabled": "#004400"},  # Насыщенный фосфор
        "Base": {"Active": "#000000", "Inactive": "#000000", "Disabled": "#000000"},
        "AlternateBase": {"Active": "#0a0a0a", "Inactive": "#0a0a0a", "Disabled": "#000000"},
        "ToolTipBase": {"Active": "#00ff33", "Inactive": "#00ff33", "Disabled": "#004400"},
        "ToolTipText": {"Active": "#000000", "Inactive": "#000000", "Disabled": "#000000"},
        "Text": {"Active": "#00ff33", "Inactive": "#00cc22", "Disabled": "#004400"},
        "Button": {"Active": "#002200", "Inactive": "#002200", "Disabled": "#001100"},
        "ButtonText": {"Active": "#00ff33", "Inactive": "#00cc22", "Disabled": "#004400"},
        "BrightText": {"Active": "#55ff55", "Inactive": "#55ff55", "Disabled": "#00aa00"},  # "Раскаленный" фосфор
        "Highlight": {"Active": "#00ff33", "Inactive": "#008822", "Disabled": "#002200"},
        "HighlightedText": {"Active": "#000000", "Inactive": "#000000", "Disabled": "#004400"},
        "Link": {"Active": "#55ff55", "Inactive": "#55ff55", "Disabled": "#004400"},
        "LinkVisited": {"Active": "#00aa00", "Inactive": "#00aa00", "Disabled": "#004400"},
        "Shadow": {"Active": "#000000", "Inactive": "#000000", "Disabled": "#000000"},
        "PlaceholderText": {"Active": "#004400", "Inactive": "#003300", "Disabled": "#001100"},
        "Accent": {"Active": "#00ff33", "Inactive": "#00cc22", "Disabled": "#004400"},
        "Light": {"Active": "#004400", "Inactive": "#004400", "Disabled": "#001100"},
        "Dark": {"Active": "#000000", "Inactive": "#000000", "Disabled": "#000000"},
        "Mid": {"Active": "#002200", "Inactive": "#002200", "Disabled": "#001100"},
        "Midlight": {"Active": "#003300", "Inactive": "#003300", "Disabled": "#002200"}
    }
}

class PaletteManager:
    def __init__(self, main_window, p_app, p_dict_colors, palette_combo):
        self.main_window = main_window
        self.app = p_app
        self.dict_themes = dict()
        self.themes = {}
        self.palette_combo: QComboBox = palette_combo
        self.palettes = dict()
        self.colors = dict()
        self.set_dict(p_dict_colors)
        self.init_them()
        style = QApplication.style()
        if style:
            self.initial_style_name = style.objectName()
        else:
            self.initial_style_name = "default"  # или любая заглушка

        self.initial_palette = QPalette(QApplication.palette())

    def set_dict(self, p_dict_colors):
        i = 1
        for theme, color in p_dict_colors.items():
            self.dict_themes[theme] = str(i)
            self.colors[str(i)] = color
            i += 1

    def reset_theme(self):
        QApplication.setPalette(self.initial_palette)
        QApplication.setStyle(QStyleFactory.create(self.initial_style_name))
        QtWidgets.QToolTip.setPalette(self.initial_palette)

    def create_palette(self, theme: str = "1") -> QtGui.QPalette:
        self.app.setStyle(APP_STYLE)
        p_palette = QtGui.QPalette()
        colors = self.colors[theme]
        # Применяем все роли и состояния

        for role_name, state_colors in colors.items():
            # Получаем enum роли
            role = getattr(QtGui.QPalette.ColorRole, role_name)

            for state_name, color_value in state_colors.items():
                # Получаем enum группы
                group = getattr(QtGui.QPalette.ColorGroup, state_name)
                p_palette.setColor(group, role, QtGui.QColor(color_value))
        return p_palette

    def init_them(self):
        for role_name, role_colors in self.dict_themes.items():
            self.palette_combo.addItem(role_name)
            self.add_theme(role_colors, role_colors)  # !!!!
        self.palette_combo.addItem("Стандартная")
        # def get_palettes(self):  # !!!
        current_style_name = self.app.style().objectName()
        styles = QtWidgets.QStyleFactory.keys()
        for style_name in styles:
            # Устанавливаем стиль
            QtWidgets.QApplication.setStyle(style_name)
            self.palettes[style_name.lower()] = self.app.style().standardPalette()
        self.app.setStyle(current_style_name)

    def add_theme(self, name: str, theme_type: str = "1"):
        """Создать и сохранить палитру по имени"""
        self.themes[name] = self.create_palette(theme_type)

    def get_palette(self, name: str) -> QtGui.QPalette:
        """Получить палитру по имени"""
        return self.themes.get(name, self.create_palette("1"))

    def set_palette(self):  # !!!
        palette_name = self.palette_combo.currentText()
        if palette_name == "Стандартная":
            self.reset_theme()
        else:
            self.apply_palette(self.dict_themes[palette_name])  # !!!

    def apply_palette(self, name: str):
        self.app.setPalette(self.themes[name])
        p_palette = self.get_palette(name)
        self.app.setPalette(p_palette)
        QtWidgets.QToolTip.setPalette(p_palette)
