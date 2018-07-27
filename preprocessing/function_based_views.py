from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import JobSerializer
from .models import Job


@api_view(['POST'])
def start_job(request):
    """

    :param request: contains field pre_process, file_id, model_id etc.
    :return:
    """

    request_dict = request.data.dict().copy()
    job_list = []
    # check if there is no file_id or model_id.
    if 'model_id' not in request_dict or 'file_id' not in request_dict:
        data = {
            "error": True,
            "errors": 'Please pass file id and model id in request.',
        }
        return Response(data, status=status.HTTP_400_BAD_REQUEST)
    model = request_dict['model_id']
    jobs = Job.objects.filter(model_id=model)
    if len(jobs) > 0:
        job = jobs[0]
        if hasattr(request_dict, 'run_all') and request_dict['run_all']:
            vsa_run('run_all')
        if 'pre_process' in request_dict and request_dict['pre_process']:
            job_list.append('pre_process')
        if 'solution_process' in request_dict and request_dict['solution_process']:
            if job.pre_process:
                request_dict['pre_process'] = True
                job_list.append('solution_process')
            else:
                data = {
                    "error": True,
                    "errors": 'Please run PreProcess first',
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
        if 'post_process' in request_dict and request_dict['post_process']:
            if job.pre_process and job.solution_process:
                request_dict['pre_process'] = True
                request_dict['solution_process'] = True
                job_list.append('post_process')
            else:
                data = {
                    "error": True,
                    "errors": 'Please run PreProcess and Solution Process first',
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
    else:
        if hasattr(request.data, 'run_all') or hasattr(request.data, 'pre_process'):
            pass
        else:
            data = {
                "error": True,
                "errors": 'Please run all jobs or PreProcess first',
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
    serializer = JobSerializer(data=request_dict)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Job Started", "id:": serializer.data['id']}, status=status.HTTP_202_ACCEPTED)
    else:
        data = {
            "error": True,
            "errors": serializer.errors,
        }
        return Response(data)


@api_view(['GET'])
def jobs(request, id):
    return Response(JobSerializer(Job.objects.filter(id=id), many=True).data)


def vsa_run(param):
    pass