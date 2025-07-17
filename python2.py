import argparse
import json
import matplotlib.pyplot as plt
import numpy as np
import os

def load_data(filename):
    """Загрузка данных из файла разных форматов"""
    ext = os.path.splitext(filename)[1].lower()
    
    if ext == '.json':
        with open(filename) as f:
            data = json.load(f)
        if 'data' in data:  
            x = [item['x'] for item in data['data']]
            y = [item['y'] for item in data['data']]
        else: 
            x = data['x']
            y = data['y']
    else:
        raise ValueError(f"Unsupported file format: {ext}")
    
    return np.array(x), np.array(y)

def plot_function(x, y, args):
    """Построение графика с учетом параметров"""
    plt.figure(figsize=(10, 6))
    

    plt.plot(x, y, label=args.legend)
    

    if args.ymin is not None and args.ymax is not None:
        plt.ylim(args.ymin, args.ymax)
    

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

    if args.output:
        plt.savefig(args.output)
    else:
        plt.show()

def main():
    parser = argparse.ArgumentParser(description='Plot function from data file')
    parser.add_argument('filename', help='Input data file')
    

    parser.add_argument('--ymin', type=float, help='Minimum Y value')
    parser.add_argument('--ymax', type=float, help='Maximum Y value')

    parser.add_argument('--output', help='Output image file')
    
    args = parser.parse_args()
    
    x, y = load_data(args.filename)
    plot_function(x, y, args)

if __name__ == '__main__':
    main()
