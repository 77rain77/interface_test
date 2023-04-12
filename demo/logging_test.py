import logging

logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s - %(lineno)d - %(message)s ',filename='1.log')
logger = logging.getLogger()
#basicConfig里的level级别： 这是设置打印日志级别，低于该级别的就不打印输出，高于的才记录。所以有必要了解这个level级别设置。在logging模块里，一共分了5个级别：
logger.info("程序开始执行...")

def cal_area(radius=None):
    return 3.14*radius*radius

radius = eval(input("请输入半径的值:"))
if radius <=0:
    logger.warning("半径不能小于0...")
logger.info("开始计算面积...")
area = cal_area(radius=radius)
logger.info("计算面积结果为:{area}".format(area=area))



