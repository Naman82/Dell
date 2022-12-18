from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from src.utils import send_response
from .seqMatcher import plagerised_ratio
# Create your views here.

# plg=Plagiarism()

class FileUploder(APIView):

    parser_classes=[MultiPartParser]

    def post(self,request,format=None):
        f1=request.FILES['file1']
        f2=request.FILES['file2']

        ext1=str(f1).split('.')[1]
        ext2=str(f2).split('.')[1]

        f1=f1.read().decode('utf-8')
        f2=f2.read().decode('utf-8')

        data=plagerised_ratio(f1,f2,ext1,ext2)

        return send_response(data=data,message="File has been uploaded successfully")
        # return HttpResponse(data)
        