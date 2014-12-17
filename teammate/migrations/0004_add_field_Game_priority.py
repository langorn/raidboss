# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Game.priority'
        db.add_column(u'teammate_game', 'priority',
                      self.gf('django.db.models.fields.IntegerField')(default=0, max_length=5),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Game.priority'
        db.delete_column(u'teammate_game', 'priority')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'teammate.attributes': {
            'Meta': {'object_name': 'Attributes'},
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['teammate.Game']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'type': ('django.db.models.fields.IntegerField', [], {})
        },
        u'teammate.character': {
            'Meta': {'object_name': 'Character'},
            'desc': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['teammate.Game']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['teammate.Job']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['teammate.Race']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'teammate.characterattr': {
            'Meta': {'object_name': 'CharacterAttr'},
            'attr': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'value': ('django.db.models.fields.IntegerField', [], {'max_length': '200'})
        },
        u'teammate.chatroom': {
            'Meta': {'object_name': 'Chatroom'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'peer_code': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user_chatroom'", 'to': u"orm['auth.User']"})
        },
        u'teammate.comment': {
            'Meta': {'object_name': 'Comment'},
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'topic_name': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'topic_name'", 'to': u"orm['teammate.Topic']"}),
            'user_name': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'topic_users'", 'to': u"orm['auth.User']"})
        },
        u'teammate.game': {
            'Meta': {'object_name': 'Game'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'post_count': ('django.db.models.fields.IntegerField', [], {'max_length': '5'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'max_length': '5'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'teammate.instance': {
            'Meta': {'object_name': 'Instance'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['teammate.Game']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'post_count': ('django.db.models.fields.IntegerField', [], {'max_length': '5'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '200'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'teammate.job': {
            'Meta': {'object_name': 'Job'},
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['teammate.Game']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'teammate.personality': {
            'Meta': {'object_name': 'Personality'},
            'by_user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'by_user'", 'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'like': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['teammate.UserType']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'from_user'", 'to': u"orm['auth.User']"})
        },
        u'teammate.race': {
            'Meta': {'object_name': 'Race'},
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['teammate.Game']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'teammate.requirement': {
            'Meta': {'object_name': 'Requirement'},
            'dpser': ('django.db.models.fields.IntegerField', [], {'max_length': '200'}),
            'games': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'topic_games'", 'to': u"orm['teammate.Game']"}),
            'healer': ('django.db.models.fields.IntegerField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tank': ('django.db.models.fields.IntegerField', [], {'max_length': '200'}),
            'teammate': ('django.db.models.fields.IntegerField', [], {'max_length': '200'}),
            'topics': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'topic_requirement'", 'to': u"orm['teammate.Topic']"})
        },
        u'teammate.skill': {
            'Meta': {'object_name': 'Skill'},
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['teammate.Game']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'teammate.topic': {
            'Instance': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['teammate.Instance']"}),
            'Meta': {'object_name': 'Topic'},
            'chatroom': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'game_name': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'topic_game'", 'to': u"orm['teammate.Game']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner_name': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'topic_targets'", 'to': u"orm['auth.User']"}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'max_length': '200'}),
            'remark': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'teammate.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'attitude': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'chatroom': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'userprofile_chatroom'", 'null': 'True', 'to': u"orm['teammate.Chatroom']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'facebook_id': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'user_profile'", 'unique': 'True', 'to': u"orm['auth.User']"})
        },
        u'teammate.usertype': {
            'Meta': {'object_name': 'UserType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'type': ('django.db.models.fields.IntegerField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['teammate']