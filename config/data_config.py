class GlobalVal:
    @classmethod
    def get_value(cls,col):
        dic={
            "id":1,
            "module":2,
            "url":3,
            "is_run":4,
            "request_method":5,
            "header":6,
            "depend_case":7,
            "depend_resp_field":8,
            "depend_field":9,
            "request_data":10,
            "exp_result":11,
            "act_result":12,
            "test_result":13,
            "exec_time":14

        }
        return dic[col]