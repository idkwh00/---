import argparse
import json
import matplotlib.pyplot as plt
import numpy as np
import xml.etree.ElementTree as ET
import csv
import os

def load_data(filename):
    """Загрузка данных из файла разных форматов"""
    ext = os.path.splitext(filename)[1].lower()
    
    if ext == '.json':
        with open(filename) as f:
            data = json.load(f)
        if 'data' in data:  # Формат 4
            x = [item['x'] for item in data['data']]
            y = [item['y'] for item in data['data']]
        else:  # Формат 3
            x = data['x']
            y = data['y']
    elif ext == '.csv':
        x, y = [], []
        with open(filename) as f:
            reader = csv.reader(f)
            next(reader)  # Пропускаем заголовок если есть
            for row in reader:
                x.append(float(row[1]))
                y.append(float(row[2]))
    elif ext == '.txt':
        x, y = [], []
        with open(filename) as f:
            for line in f:
                parts = line.strip().split('    ')
                x.append(float(parts[0]))
                y.append(float(parts[1]))
    elif ext == '.xml':
        tree = ET.parse(filename)
        root = tree.getroot()
        if root.find('xdata') is not None:  # Формат 5
            x = [float(elem.text) for elem in root.find('xdata')]
            y = [float(elem.text) for elem in root.find('ydata')]
        else:  # Формат 6
            x = [float(row.find('x').text) for row in root.findall('row')]
            y = [float(row.find('y').text) for row in root.findall('row')]
    else:
        raise ValueError(f"Unsupported file format: {ext}")
    
    return np.array(x), np.array(y)

def plot_function(x, y, args):
    """Построение графика с учетом параметров"""
    plt.figure(figsize=(10, 6))
    
    # Основной график
    plt.plot(x, y, label=args.legend)
    
    # Настройка осей Y
    if args.ymin is not None and args.ymax is not None:
        plt.ylim(args.ymin, args.ymax)
    
    # Дополнительные настройки
    if args.title:
        plt.title(args.title)
    if args.xlabel:
        plt.xlabel(args.xlabel)
    if args.ylabel:
        plt.ylabel(args.ylabel)
    if args.grid:
        plt.grid(True)
    
    if args.legend:
        plt.legend()
    
    # Сохранение или отображение
    if args.output:
        plt.savefig(args.output)
    else:
        plt.show()

def main():
    parser = argparse.ArgumentParser(description='Plot function from data file')
    parser.add_argument('filename', help='Input data file')
    
    # Основные параметры графика
    parser.add_argument('--title', help='Title of the plot')
    parser.add_argument('--xlabel', help='Label for X axis')
    parser.add_argument('--ylabel', help='Label for Y axis')
    parser.add_argument('--legend', help='Legend text')
    parser.add_argument('--grid', action='store_true', help='Enable grid')
    
    # Параметры для варианта 4 (оси Y)
    parser.add_argument('--ymin', type=float, help='Minimum Y value')
    parser.add_argument('--ymax', type=float, help='Maximum Y value')
    
    # Дополнительные параметры
    parser.add_argument('--output', help='Output image file')
    
    args = parser.parse_args()
    
    # Загрузка данных и построение графика
    x, y = load_data(args.filename)
    plot_function(x, y, args)

if __name__ == '__main__':
    main()