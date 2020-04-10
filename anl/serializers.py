import serpy
from rest_framework import serializers
from forward_and_spot.models import Auction, Treatment, Group, Offer, Player, Player_stats,Phase, Period

# put ANL in its own app?
# complete serializers used for data transfers to ANL app
class AnlOfferSer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = "__all__"


class AnlPeriodSer(serializers.ModelSerializer):
    class Meta:
        model = Period
        fields = "__all__"


class AnlPhaseSer(serializers.ModelSerializer):
    class Meta:
        model = Phase
        fields = "__all__"


class AnlPlayerSer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = "__all__"


class AnlTreatmentSer(serializers.ModelSerializer):
    class Meta:
        model = Treatment
        fields = "__all__"

class AnlAuctionSer(serializers.ModelSerializer):
    class Meta:
        model = Auction
        fields = "__all__"

class AnlPlayerStatsSer(serializers.ModelSerializer):
    class Meta:
        model = Player_stats
        fields = "__all__"

class AnlGroupStatsSer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"
