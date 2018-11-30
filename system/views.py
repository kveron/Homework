from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "index.html"


class NirvanaSmells(TemplateView):
    template_name = "1.1.html"


class NirvanaHeart(TemplateView):
    template_name = "1.2.html"


class NirvanaMan(TemplateView):
    template_name = "1.3.html"


class GreenAmerican(TemplateView):
    template_name = "2.1.html"


class GreenDreams(TemplateView):
    template_name = "2.2.html"


class GreenWake(TemplateView):
    template_name = "2.3.html"


class ParkNumb(TemplateView):
    template_name = "3.1.html"


class ParkEnd(TemplateView):
    template_name = "3.2.html"


class ParkDone(TemplateView):
    template_name = "3.3.html"


class AcBlack(TemplateView):
    template_name = "4.1.html"


class AcHell(TemplateView):
    template_name = "4.2.html"


class AcThunder(TemplateView):
    template_name = "4.3.html"


class GracePain(TemplateView):
    template_name = "5.1.html"


class GraceMachine(TemplateView):
    template_name = "5.2.html"


class GraceRace(TemplateView):
    template_name = "5.3.html"


