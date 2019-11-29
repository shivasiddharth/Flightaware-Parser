#!/usr/bin/python3
# -*- coding: utf-8 -*-
from datetime import datetime, timezone
import json
import urllib.request
import requests
import re


class fascrapper:

    def __init__(self):
        self.urlbase = 'https://www.flightaware.com/live/'
        self.flightnum = ''
        self.aircrafttype = ''
        self.flightorg = ''
        self.flightdest = ''
        self.flightstatus = ''
        self.estgatedep = ''
        self.esttakeoff = ''
        self.estland = ''
        self.estgatearriv = ''
        self.actgatedep = ''
        self.acttakeoff = ''
        self.actland = ''
        self.actgatearriv = ''
        self.aircraftposition = ''
        self.alt = ''
        self.gspd = ''

    def gettime(self, epochtime):
        if epochtime != None and epochtime != []:
            gmttime = \
                datetime.utcfromtimestamp(epochtime).strftime('%B %d %Y %H:%M:%S'
                    )
        else:
            gmttime = epochtime
        return gmttime

    def faextract(self, flightno):
        faresponse = urllib.request.urlopen(self.urlbase + 'flight/'
                + flightno)
        fawebcontent = faresponse.read()
        fawebcontent = fawebcontent.decode('utf-8')
        faidx1 = fawebcontent.find('trackpollBootstrap = ')
        facontent = fawebcontent[faidx1 + 21:]
        faidx2 = facontent.find(';</script>')
        facontent = facontent[:faidx2]
        facontent.replace(';</script>', '', 1)
        facontent = facontent.strip()
        facontent = json.loads(facontent)
        return facontent

    def flightdata(self, flightcode):
        fldet = self.faextract(flightcode)
        flightkey = list(fldet['flights'].keys())
        self.flightnum = fldet['flights'][flightkey[0]]['friendlyIdent']
        self.flightstatus = fldet['flights'
                                  ][flightkey[0]]['flightStatus']
        self.aircrafttype = fldet['flights'][flightkey[0]]['aircraft'
                ]['friendlyType']
        self.flightorg = fldet['flights'][flightkey[0]]['origin'
                ]['friendlyLocation']
        self.flightdest = fldet['flights'][flightkey[0]]['destination'
                ]['friendlyLocation']
        self.estgatedep = fldet['flights'
                                ][flightkey[0]]['gateDepartureTimes'
                ]['estimated']
        self.esttakeoff = fldet['flights'][flightkey[0]]['takeoffTimes'
                ]['estimated']
        self.estland = fldet['flights'][flightkey[0]]['landingTimes'
                ]['estimated']
        self.estgatearriv = fldet['flights'
                                  ][flightkey[0]]['gateArrivalTimes'
                ]['estimated']
        self.estgatedep = self.gettime(fldet['flights'
                ][flightkey[0]]['gateDepartureTimes']['estimated'])
        self.esttakeoff = self.gettime(fldet['flights'
                ][flightkey[0]]['takeoffTimes']['estimated'])
        self.estland = self.gettime(fldet['flights'
                                    ][flightkey[0]]['landingTimes'
                                    ]['estimated'])
        self.estgatearriv = self.gettime(fldet['flights'
                ][flightkey[0]]['gateArrivalTimes']['estimated'])
        self.actgatedep = self.gettime(fldet['flights'
                ][flightkey[0]]['gateDepartureTimes']['actual'])
        self.acttakeoff = self.gettime(fldet['flights'
                ][flightkey[0]]['takeoffTimes']['actual'])
        self.actland = self.gettime(fldet['flights'
                                    ][flightkey[0]]['landingTimes'
                                    ]['actual'])
        self.actgatearriv = self.gettime(fldet['flights'
                ][flightkey[0]]['gateArrivalTimes']['actual'])
        self.alt = fldet['flights'][flightkey[0]]['altitude']
        self.gspd = fldet['flights'][flightkey[0]]['groundspeed']
        if self.flightstatus == 'airborne':
            if self.actgatedep == None:
                self.distcov = ''
                self.distrem = ''
                self.aircraftposition = 'Unkown'
            elif self.actgatedep != None and self.acttakeoff == None:
                self.distcov = ''
                self.distrem = ''
                self.aircraftposition = \
                    'Departed gate. Taxiing for takeoff'
            elif self.actgatedep != None and self.acttakeoff != None:
                self.distcov = fldet['flights'][flightkey[0]]['distance'
                        ]['elapsed']
                self.distrem = fldet['flights'][flightkey[0]]['distance'
                        ]['remaining']
                self.aircraftposition = 'In air, covered ' \
                    + str(self.distcov) + ' nautical miles with ' \
                    + str(self.distrem) + ' nautical miles remaining.'
        elif self.flightstatus == 'arrived':
            if self.actland == None:
                self.aircraftposition = 'Unkown'
            elif self.actland != None and self.actgatearriv == None:
                self.aircraftposition = \
                    'Arrived at destination. Taxiing to gate'
            elif self.actland != None and self.actgatearriv != None:
                self.aircraftposition = \
                    'Arrived at destination and at the gate'
            else:
                self.aircraftposition = 'Unkown'
        elif self.flightstatus == None or self.flightstatus == '':
            self.aircraftposition = 'Unkown'
        else:
            self.aircraftposition = 'Unkown'
        return (
            self.flightnum,
            self.aircrafttype,
            self.flightorg,
            self.flightdest,
            self.flightstatus,
            self.alt,
            self.gspd,
            self.estgatedep,
            self.esttakeoff,
            self.estland,
            self.estgatearriv,
            self.actgatedep,
            self.acttakeoff,
            self.actland,
            self.actgatearriv,
            self.aircraftposition,
            )
