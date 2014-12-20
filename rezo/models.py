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

from django.db import models

#class Bannissements(models.Model):
#    id = models.IntegerField(primary_key=True)
#    utilisateur_id = models.IntegerField()
#    rezoteur_id = models.IntegerField()
#    timestampdebut = models.IntegerField(db_column='timestampDebut')
#    timestampfin = models.IntegerField(db_column='timestampFin')
#    typeraison = models.CharField(db_column='typeRaison', max_length=10)
#    raison = models.TextField()
#    class Meta:
#        managed = False
#        db_table = 'bannissements'
#
#class Banques(models.Model):
#    id = models.IntegerField(primary_key=True)
#    nom = models.TextField()
#    class Meta:
#        managed = False
#        db_table = 'banques'
#
#class Blocs(models.Model):
#    id = models.IntegerField(primary_key=True)
#    nom = models.TextField()
#    description = models.TextField()
#    ipdebut = models.CharField(db_column='ipDebut', max_length=15)
#    ipfin = models.CharField(db_column='ipFin', max_length=15)
#    alloueesparpaijiadmin = models.CharField(
#        db_column='alloueesParPaijiAdmin', max_length=1
#   )
#    class Meta:
#        managed = False
#        db_table = 'blocs'
#
#class Documents(models.Model):
#    id = models.IntegerField(primary_key=True)
#    nomdocument = models.TextField(db_column='nomDocument')
#    descriptiondocument = models.TextField(db_column='descriptionDocument')
#    class Meta:
#        managed = False
#        db_table = 'documents'
#
#class DocumentsEcoles(models.Model):
#    id = models.IntegerField(primary_key=True)
#    document_id = models.IntegerField()
#    ecole_id = models.IntegerField()
#    commentaires = models.TextField()
#    class Meta:
#        managed = False
#        db_table = 'documents_ecoles'
#
#class DocumentsUtilisateurs(models.Model):
#    id = models.IntegerField(primary_key=True)
#    document_id = models.IntegerField()
#    utilisateur_id = models.IntegerField()
#    rezoteur_id = models.IntegerField()
#    timestamp = models.IntegerField()
#    secrpointage = models.IntegerField(db_column='secrPointage')
#    class Meta:
#        managed = False
#        db_table = 'documents_utilisateurs'
#


class Ecole(models.Model):
    id = models.IntegerField(primary_key=True)
    nom = models.TextField(db_column='nomEcole')
    description = models.TextField(db_column='descriptionEcole')
    rezotable = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'ecoles'

#class Events(models.Model):
#    id = models.IntegerField(primary_key=True)
#    utilisateur_id = models.IntegerField()
#    rezoteur_id = models.IntegerField()
#    timestamp = models.IntegerField()
#    commentaires = models.TextField()
#    class Meta:
#        managed = False
#        db_table = 'events'
#
class Paiements(models.Model):
    id = models.IntegerField(primary_key=True)
    utilisateur_id = models.IntegerField()
    rezoteur_id = models.IntegerField()
    timestamp = models.IntegerField()
    moyenpaiement = models.CharField(db_column='moyenPaiement', max_length=7)
    banque_id = models.IntegerField()
    chknumero = models.IntegerField(db_column='chkNumero')
    trezpointage = models.IntegerField(db_column='trezPointage')
    commentaires = models.TextField()
    class Meta:
        managed = False
        db_table = 'paiements'

class PaiementsVentilations(models.Model):
    id = models.IntegerField(primary_key=True)
    paiement_id = models.IntegerField()
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    prixunitaire = models.DecimalField(
       db_column='prixUnitaire', max_digits=10, decimal_places=2
    )
    affectation = models.CharField(max_length=10)
    class Meta:
        managed = False
        db_table = 'paiements_ventilations'
#
#
#class Rezoswitches(models.Model):
#    id = models.IntegerField(primary_key=True)
#    equipement_id = models.IntegerField()
#    nombreport = models.IntegerField(db_column='nombrePort')
#    infos = models.TextField()
#    localisation = models.CharField(max_length=100)
#    class Meta:
#        managed = False
#        db_table = 'rezoswitches'
#
#class Rezoteurs(models.Model):
#    id = models.IntegerField(primary_key=True)
#    utilisateur_id = models.IntegerField()
#    login = models.TextField()
#    password = models.TextField()
#    droits = models.CharField(max_length=2)
#    actif = models.CharField(max_length=1)
#    class Meta:
#        managed = False
#        db_table = 'rezoteurs'
#
#class Topologies(models.Model):
#    id = models.IntegerField(primary_key=True)
#    rezoswitch_id = models.IntegerField()
#    port = models.IntegerField()
#    type = models.CharField(max_length=7)
#    nom = models.CharField(max_length=50)
#    idswitchconnecte = models.IntegerField(db_column='idSwitchConnecte')
#    equipement_id = models.IntegerField()
#    class Meta:
#        managed = False
#        db_table = 'topologies'


class Utilisateur(models.Model):
    id = models.IntegerField(primary_key=True)
    ecole = models.ForeignKey(Ecole, to_field="id")
    precisionecole = models.TextField(db_column='precisionEcole')
    nom = models.TextField()
    prenom = models.TextField()
    topology_id = models.IntegerField(blank=True, null=True)
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
        Utilisateur, to_field="id", unique=True,
        db_column='id', related_name="quotas",
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


from django.contrib.auth.models import AbstractUser
from django.utils.functional import cached_property
from django.core.urlresolvers import reverse

from modular_blocks.models import TwoModularColumnsMixin

from home.middleware import UserAuthGroupMixin


class User(UserAuthGroupMixin, TwoModularColumnsMixin, AbstractUser):
    id_rezo = models.PositiveIntegerField(null=True, default=0)

    @cached_property
    def get_rezo(self):
        return Utilisateur.objects.using('rezo').select_related('quotas').get(
            pk=self.id_rezo,
        )
        
    @cached_property
    def get_paiements(self):
        return Utilisateur.objects.using('rezo').select_related('quotas').get(
            pk=self.id_rezo,
        )

    @cached_property
    def get_related_groups(self):
        posts = self.post.all()
        groups = []
        for post in posts:
            groups.append(post.bureau.group)
        return groups

    def get_absolute_url(self):
        return reverse('index')
