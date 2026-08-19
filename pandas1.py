#import pandas as pd
#import numpy as np
#d2=[10,20,30]
#d1=pd.DataFrame(d2)
#print(d1)
#print(d1.ndim)
#working with series module
import pandas as pd
d1=[10,20,30,40]
d2=pd.Series(d1)
print(d2)

import pandas as pd
d1={[10,20,30,40],index:['a','b','c','d']}
d2=pd.Series(d1)
print(d2)