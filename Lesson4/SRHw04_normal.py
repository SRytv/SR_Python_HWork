
# �������-1:
# ������� ������� � ������ ��������, ������� ��������� ������
# 1 ��� ����� �������� � ������� ��������.
# �.�. �� ������ "mtMmEZUOmcq" ����� �������� ['mt', 'm', 'mcq']
# ������ ������ ����� ���������: � ������� re � ���.

line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNO'\
       'GIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzK'\
       'TUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqn'\
       'LxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIVjXa'\
       'pzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnWete'\
       'kUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfCvzQ'\
       'WrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXb'\
       'JrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCC'\
       'EUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfB'\
       'tQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuT'\
       'SkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCfKCu'\
       'UJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWHuXB'\
       'qHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFa'\
       'XiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQ'\
       'zTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'

#===============================================================================
import re
pattern = re.compile(r'[a-z]{2}([A-Z])[A-Z]{2}')
result = pattern.findall(line)
print (result)
"""
[line[i] for i in range(1,(len(line)-1)) if (65< ord(line[i] and ord(line[i])< 90) and
(97< ord(line[i-2]) and ord(line[i-2])< 122) and
(97< ord(line[i-1]) and ord(line[i-1])< 122) and
(65< ord(line[i+1]) and ord([line[i+1])< 90) and
#PyCharm ������ ��������� ����� � ord([line[i+1])< 90) ����� '] ����������:"expected ','' or ']'
(65< ord(line[i+2]) and ord(line[i+2])< 90)]
#� �����: ����� ord(line[i+2])< 90) ����� ��������� ����������� ']' ����� ord(line[i+2])< 90) ")": "expected ')' or ']', ���� ��� ������ ��� "��������..."
"""

#===============================================================================

# �������-2:
# ������� ������� � ������� ��������, ����� �� ������� ���������
# ��� ������� � ������ ��������, � ������ - ��� ������� � ������� ��������.
# �.�. �� ������ 
# "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# ����� �������� ������ �����: ['AY', 'NOGI', 'P']
# ������ ������ ����� ���������: � ������� re � ���.

line_2 = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysm'\
       'NOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewV'\
       'fzKTUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSA'\
       'HqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIV'\
       'jXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnW'\
       'etekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfC'\
       'vzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbR'\
       'uXbJrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkm'\
       'jCCEUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOn'\
       'LfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGS'\
       'euTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCf'\
       'KCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWH'\
       'uXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQN'\
       'JFaXiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQ'\
       'oiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGC'
#===============================================================================
iimport re
pattern = re.compile(r'[a-z]{2}([A-Z]*)[A-Z]{2}')
result = pattern.findall(line_2)
#print (result)
result2 =  [x for x in result if x != ''] #  �������� ������ �����: ����������� ��������������� '*'
print(result2)
"""
[line_2[i] for i in range(2,(len(line_2)-2)) if (65< ord(line_2[i]) and ord(line_2[i])< 90) and
(97< ord(line_2[i-2]) and (ord(line_2[i-2])< 122) and
(97< ord(line_2[i-1]) and ord(line_2[i-1])< 122) and
(65< ord(line_2[i+1]) and ord([line_2[+1])< 90) and
(65< ord(line_2[i+2]) and ord(line_2[i+2])< 90)]
#����� � ������ �� ������ , �� �� ��������???!!! :�(
"""


#===============================================================================

# �������-3:
# �������� ������, ����������� ��������� ���� (�������������� ������� ��� �����)
# ������������� ������ �������, � ���������� � ����� ������ ����
# 2500-������� ������������ �����.
# ������� � �������� ����� ������� ������������������ ���������� ����
# � ��������������� �����.