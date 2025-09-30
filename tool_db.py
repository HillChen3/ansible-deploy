import pymysql
import yaml


def getConnect():
    try:
        with open('config.yml', 'r') as f:
            result = yaml.load(f, Loader=yaml.FullLoader)
            mysqlresult = result['mysql']

        # 修复：使用关键字参数而非位置参数[1,4](@ref)
        connect = pymysql.connect(
            host=mysqlresult['host'],
            user=mysqlresult['username'],  # 注意：参数名是user不是username
            password=mysqlresult['password'],
            database=mysqlresult['database'],
            port=mysqlresult['port'],
            charset='utf8mb4'  # 添加字符集避免编码问题[1](@ref)
        )
        return connect
    except Exception as e:
        print(f"数据库连接失败: {e}")
        return None  # 确保返回None而不是让异常传播


def selectByParameters(sql, params=None):
    connect = None
    cursor = None
    try:
        connect = getConnect()
        if connect is None:
            print("无法建立数据库连接")
            return None

        cursor = connect.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql, params)
        result = cursor.fetchall()
        return result
    except Exception as e:
        print(f"查询错误: {e}")
        return None
    finally:
        # 修复：安全地关闭资源[9](@ref)
        if cursor:
            cursor.close()
        if connect:
            connect.close()


def updateByParameters(sql, params=None):
    connect = None
    cursor = None
    try:
        connect = getConnect()
        if connect is None:
            print("无法建立数据库连接")
            return None

        cursor = connect.cursor(pymysql.cursors.DictCursor)
        count = cursor.execute(sql, params)
        connect.commit()
        return count
    except Exception as e:
        # 修复：只有在连接成功时才回滚[9](@ref)
        if connect:
            connect.rollback()
        print(f"更新错误: {e}")
        return None
    finally:
        if cursor:
            cursor.close()
        if connect:
            connect.close()


if __name__ == "__main__":
    sql = "delete from servers where id = %s"
    result = updateByParameters(sql, params=(3,))
    print(result)