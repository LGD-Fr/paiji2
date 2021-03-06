# -*- encoding: utf-8 -*- #
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines for those models you wish to give
#     write DB access
# Feel free to rename the models, but don't rename db_table values or
#   field names.
#
# Also note: You'll have to insert the output of
#    'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals
from datetime import datetime, timedelta
# from calendar import monthrange

from django.db import models
# from django.utils.timezone import now
from django.contrib.auth.models import AbstractUser
from django.utils.functional import cached_property
from django.core.urlresolvers import reverse
from django.conf import settings
# from django.utils.translation import ugettext as _

from modular_blocks.models import (
    TwoModularColumnsMixin,
    TopModularColumnMixin,
)

from home.middleware import UserAuthGroupMixin


# class Bannissements(models.Model):
#     id = models.IntegerField(primary_key=True)
#     utilisateur_id = models.IntegerField()
#     rezoteur_id = models.IntegerField()
#     timestampdebut = models.IntegerField(db_column='timestampDebut')
#     timestampfin = models.IntegerField(db_column='timestampFin')
#     typeraison = models.CharField(db_column='typeRaison', max_length=10)
#     raison = models.TextField()
#     class Meta:
#         managed = False
#         db_table = 'bannissements'
#
# class Banques(models.Model):
#     id = models.IntegerField(primary_key=True)
#     nom = models.TextField()
#     class Meta:
#         managed = False
#         db_table = 'banques'
#
# class Blocs(models.Model):
#     id = models.IntegerField(primary_key=True)
#     nom = models.TextField()
#     description = models.TextField()
#     ipdebut = models.CharField(db_column='ipDebut', max_length=15)
#     ipfin = models.CharField(db_column='ipFin', max_length=15)
#     alloueesparpaijiadmin = models.CharField(
#         db_column='alloueesParPaijiAdmin', max_length=1
#    )
#     class Meta:
#         managed = False
#         db_table = 'blocs'
#
# class Documents(models.Model):
#     id = models.IntegerField(primary_key=True)
#     nomdocument = models.TextField(db_column='nomDocument')
#     descriptiondocument = models.TextField(db_column='descriptionDocument')
#     class Meta:
#         managed = False
#         db_table = 'documents'
#
# class DocumentsEcoles(models.Model):
#     id = models.IntegerField(primary_key=True)
#     document_id = models.IntegerField()
#     ecole_id = models.IntegerField()
#     commentaires = models.TextField()
#     class Meta:
#         managed = False
#         db_table = 'documents_ecoles'
#
# class DocumentsUtilisateurs(models.Model):
#     id = models.IntegerField(primary_key=True)
#     document_id = models.IntegerField()
#     utilisateur_id = models.IntegerField()
#     rezoteur_id = models.IntegerField()
#     timestamp = models.IntegerField()
#     secrpointage = models.IntegerField(db_column='secrPointage')
#     class Meta:
#         managed = False
#         db_table = 'documents_utilisateurs'
#


class Ecole(models.Model):
    id = models.IntegerField(
        primary_key=True,
    )
    nom = models.TextField(
        db_column='nomEcole',
    )
    description = models.TextField(
        db_column='descriptionEcole',
    )
    rezotable = models.CharField(
        max_length=1,
    )

    def __unicode__(self):
        return unicode(self.nom)

    class Meta:
        managed = False
        db_table = 'ecoles'

# class Events(models.Model):
#     id = models.IntegerField(primary_key=True)
#     utilisateur_id = models.IntegerField()
#     rezoteur_id = models.IntegerField()
#     timestamp = models.IntegerField()
#     commentaires = models.TextField()
#     class Meta:
#         managed = False
#         db_table = 'events'
#
#
#
# class Rezoswitches(models.Model):
#     id = models.IntegerField(primary_key=True)
#     equipement_id = models.IntegerField()
#     nombreport = models.IntegerField(db_column='nombrePort')
#     infos = models.TextField()
#     localisation = models.CharField(max_length=100)
#     class Meta:
#         managed = False
#         db_table = 'rezoswitches'
#
# class Rezoteurs(models.Model):
#     id = models.IntegerField(primary_key=True)
#     utilisateur_id = models.IntegerField()
#     login = models.TextField()
#     password = models.TextField()
#     droits = models.CharField(max_length=2)
#     actif = models.CharField(max_length=1)
#     class Meta:
#         managed = False
#         db_table = 'rezoteurs'
#


class Topologies(models.Model):
    id = models.IntegerField(primary_key=True)
    rezoswitch_id = models.IntegerField()
    port = models.IntegerField()
    type = models.CharField(max_length=7)
    nom = models.CharField(max_length=50)
    idswitchconnecte = models.IntegerField(db_column='idSwitchConnecte')
    equipement_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'topologies'


class Utilisateur(models.Model):
    id = models.IntegerField(primary_key=True)
    ecole = models.ForeignKey(Ecole, to_field='id')
    precisionecole = models.TextField(db_column='precisionEcole')
    nom = models.TextField()
    prenom = models.TextField()
    # topology_id = models.IntegerField(blank=True, null=True)
    topology = models.ForeignKey(Topologies, db_column='topology_id')
    email = models.TextField()
    emailverifie = models.TextField(db_column='emailVerifie')
    borne_id = models.IntegerField()
    timestamprezotage = models.IntegerField(db_column='timestampRezotage')
    rezoteur_id = models.IntegerField()
    autorisationdecouvert = models.IntegerField(
        db_column='autorisationDecouvert'
    )
    raisondecouvert = models.TextField(db_column='raisonDecouvert')
    etat = models.CharField(max_length=14)
    typeutilisateur = models.CharField(
        db_column='typeUtilisateur', max_length=11
    )

    class Meta:
        managed = False
        db_table = 'utilisateurs'


class Quotas(models.Model):
    utilisateur = models.OneToOneField(
        Utilisateur,
        db_column='id',
        to_field='id',
        primary_key=True,
        related_name="quotas",
    )
    restant_veille_in = models.BigIntegerField()
    restant_veille_out = models.BigIntegerField()
    conso_in = models.BigIntegerField()
    conso_out = models.BigIntegerField()
    web_in = models.BigIntegerField()
    web_out = models.BigIntegerField()
    warning = models.CharField(max_length=10)

    def up_restant(self):
        return self.restant_veille_out - self.conso_out

    def down_restant(self):
        return self.restant_veille_in - self.conso_in

    class Meta:
        managed = False
        db_table = 'quotas'


class Equipement(models.Model):
    id = models.IntegerField(primary_key=True)
    utilisateur = models.ForeignKey(
        Utilisateur, to_field="id",
        db_column="utilisateur_id", related_name='equipements',
    )
    ip = models.CharField(max_length=15)
    dns = models.TextField()
    dnsrez = models.TextField()
    etat = models.CharField(max_length=14)
    timestampenregistrement = models.IntegerField(
        db_column='timestampEnregistrement',
    )
    timestampdesactivationdefinitive = models.IntegerField(
        db_column='timestampDesactivationDefinitive',
    )
    type_equip = models.CharField(
        db_column='typeEquipement', max_length=16, blank=True,
    )

    class Meta:
        managed = False
        db_table = 'equipements'


class Macs(models.Model):
    id = models.IntegerField(primary_key=True)
    address = models.CharField(max_length=17, db_column="mac")
    equipement = models.ForeignKey(
        Equipement, db_column="equipement_id", related_name='mac',
    )
    description = models.TextField()
    etat = models.CharField(max_length=14)
    timestamplasttimeup = models.IntegerField(
        db_column='timestampLastTimeUp',
    )

    class Meta:
        managed = False
        db_table = 'macs'


class AccountRecovery(models.Model):
    id_rezo = models.PositiveIntegerField()
    date = models.DateTimeField()
    code = models.CharField(max_length=120)
    email = models.EmailField()


class Paiements(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(
        Utilisateur,
        to_field='id',
        db_column='utilisateur_id',
        related_name='paiements',
    )
    rezoteur_id = models.IntegerField()
    timestamp = models.IntegerField()
    moyenpaiement = models.CharField(
        db_column='moyenPaiement',
        max_length=7,
    )
    banque_id = models.IntegerField()
    chknumero = models.IntegerField(db_column='chkNumero')
    trezpointage = models.IntegerField(db_column='trezPointage')
    commentaires = models.TextField()

    class Meta:
        managed = False
        db_table = 'paiements'


class PaiementsVentilations(models.Model):
    id = models.IntegerField(primary_key=True)
    paiement_id = models.ForeignKey(
        Paiements,
        to_field='id',
        db_column='paiement_id',
        related_name='paiements_ventilations',
    )
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    prixunitaire = models.DecimalField(
        db_column='prixUnitaire', max_digits=10, decimal_places=2
    )
    affectation = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'paiements_ventilations'


class User(
    UserAuthGroupMixin,
    TopModularColumnMixin,
    TwoModularColumnsMixin,
    AbstractUser
):
    id_rezo = models.PositiveIntegerField(null=True, default=0)

    @cached_property
    def get_rezo(self):
        try:
            return Utilisateur.objects.using(
                'rezo',
                ).select_related(
                'quotas',
                ).get(
                pk=self.id_rezo,
            )
        except:
            print('Could not fetch rezo profile')
            return None

    room = models.CharField(
        null=True,
        default=None,
        max_length=50,
    )

    @cached_property
    def get_room(self):
        try:
            if self.get_rezo.etat == 'STATE_ACTIVE':
                return self.get_rezo.topology.nom
            else:
                return '~'
        except:
            print('unable to contact the database')
            return None

    @cached_property
    def expire_on(self):
        try:

            end_date = datetime.min

            payments = Paiements.objects.using('rezo').filter(
                user=self.id_rezo
            ).order_by('timestamp')

            unit_price = 0
            virt_amount = 0
            for payment in payments:
                # date at which the payment has been made
                pay_day = datetime.fromtimestamp(payment.timestamp)
                virt_amount = 0.0

                if pay_day > end_date:
                    end_date = pay_day

                # Starting from 01/08/2014, the number of paying months goes
                # from 10 to 8
                if pay_day > datetime(2014, 8, 1):
                    yearly_paying_months = 8
                else:
                    yearly_paying_months = 10

                for vent in payment.paiements_ventilations.all():
                    if not unit_price:
                        # Cast everything to float to avoid pb weird Decimal
                        unit_price = float(vent.prixunitaire)

                    if vent.affectation == "COTISATION":
                        montant = float(vent.montant)
                        while montant > 0:
                            if montant >= yearly_paying_months * unit_price:
                                virt_amount += 12 * unit_price
                                montant -= yearly_paying_months * unit_price
                            else:
                                virt_amount += montant
                                montant = 0

                end_date += timedelta(
                    int(365.25/12 * (virt_amount / unit_price))
                )

            return end_date

        except Exception as ex:
            print('Could not compute expiration date')
            return None

    @cached_property
    def cotisation_warning(self):
        try:
            date_start_alert = datetime.today() - datetime.timedelta(day=15)
            return self.expire_on() > date_start_alert
        except:
            return True

    @cached_property
    def get_related_groups(self):
        posts = self.posts.all()
        groups = []
        for post in posts:
            groups.append(post.bureau.group)
        return groups

    def get_absolute_url(self):
        return reverse('index')

    def save(self, *args, **kwargs):
        # can't have an empty sidebar...
        if self.sidebar_left is None or len(self.sidebar_left) == 0:
            if not isinstance(settings.SIDEBAR_LEFT, list):
                self.sidebar_left = [u'survey-form', u'cov', ]
            elif (
                False in
                [isinstance(i, unicode) for i in settings.SIDEBAR_LEFT]
            ):
                self.sidebar_left = [u'survey-form', u'cov', ]
            else:
                self.sidebar_left = settings.SIDEBAR_LEFT

        if self.sidebar_right is None or len(self.sidebar_right) == 0:
            if not isinstance(settings.SIDEBAR_RIGHT, list):
                self.sidebar_right = [u'rezo-account', u'bulletin-board', ]
            elif (
                False in
                [isinstance(i, unicode) for i in settings.SIDEBAR_RIGHT]
            ):
                self.sidebar_right = [u'rezo-account', u'bulletin-board', ]
            else:
                self.sidebar_right = settings.SIDEBAR_RIGHT

        return super(User, self).save(*args, **kwargs)

    class Meta:
        ordering = ('username', )


def update_user_rooms():
    print("update_user_room not implemented")
    pass
    # users = User.objects.all()
    # for user in users:
    #     got_room = user.get_room
    #     if got_room is not None:
    #         user.room = got_room
    #         user.save()
