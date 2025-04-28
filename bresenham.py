def bresenham_line(x0, y0, x1, y1):
    """Bresenham直线算法生成器，返回直线路径上的所有坐标点
    
    Args:
        x0, y0: 起始点坐标
        x1, y1: 结束点坐标
        
    Yields:
        生成器返回连续的(x, y)坐标元组
    """
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    
    # 确定步长方向
    step_x = 1 if x0 < x1 else -1
    step_y = 1 if y0 < y1 else -1
    
    error = dx - dy  # 误差累计值
    
    while True:
        yield (x0, y0)
        
        # 到达终点时终止
        if x0 == x1 and y0 == y1:
            break
            
        double_error = 2 * error
        
        # 根据误差调整坐标
        if double_error > -dy:
            error -= dy
            x0 += step_x
            
        if double_error < dx:
            error += dx
            y0 += step_y


# ========== 使用示例 ==========
if __name__ == "__main__":
    # 示例1: 打印坐标点
    print("直线(3,2)到(12,6)的坐标点:")
    for pt in bresenham_line(3, 2, 12, 6):
        print(pt)

    # 示例2: ASCII图形演示
    print("\nASCII直线演示（坐标系原点在左上角）:")
    width, height = 15, 8
    start = (3, 2)
    end = (12, 6)
    
    # 初始化画布
    canvas = [['.' for _ in range(width)] for _ in range(height)]
    
    # 绘制直线
    for x, y in bresenham_line(*start, *end):
        if 0 <= x < width and 0 <= y < height:
            canvas[y][x] = '#'
    
    # 显示结果
    for row in canvas:
        print(' '.join(row))