// Copyright (c) 2017 Zededa, Inc.
// All rights reserved.

// Type defintions for interface from Zedmanager to IdentityMgr for EID
// allocation and status

package types

import (
	"fmt"
	"log"
	"net"
	"time"
)

// Parameters which determine whether and how the EID is allocated
type EIDAllocation struct {
	Allocate            bool
	ExportPrivate       bool   // Provide private key to ZedManager
	AllocationPrefix    []byte // Normally and default 0xfd
	AllocationPrefixLen int    // Normally and default 8
}

// Indexed by UUID plus IID; version not included in index
// Implies a given App Instance can not have multiple interfaces to the same IID.
type EIDConfig struct {
	UUIDandVersion UUIDandVersion
	DisplayName    string
	EIDConfigDetails
}

type EIDConfigDetails struct {
	IID uint32
	EIDAllocation
	// When Allocate is false the ZedCloud provides these parameters.
	// No work for IdentityMgr in that case.
	// When Allocate is true these fields are not set in the config
	EID           net.IP
	LispSignature string
	PemCert       []byte
	PemPrivateKey []byte
}

func (config EIDConfig) VerifyFilename(fileName string) bool {
	expect := fmt.Sprintf("%s:%d.json",
		config.UUIDandVersion.UUID.String(), config.IID)
	ret := expect == fileName
	if !ret {
		log.Printf("Mismatch between filename and contained uuid/iid: %s vs. %s\n",
			fileName, expect)
	}
	return ret
}

// Indexed by UUID plus IID. Version is not part of the index.
type EIDStatus struct {
	UUIDandVersion UUIDandVersion
	DisplayName    string
	EIDStatusDetails
}

type EIDStatusDetails struct {
	IID uint32
	EIDAllocation
	PendingAdd    bool
	PendingModify bool
	PendingDelete bool
	EID           net.IP
	LispSignature string
	PemCert       []byte
	PemPublicKey  []byte
	PemPrivateKey []byte    // If ExportPrivate. XXX or in separate type?
	CreateTime    time.Time // When EID was created
}

func (status EIDStatus) VerifyFilename(fileName string) bool {
	expect := fmt.Sprintf("%s:%d.json",
		status.UUIDandVersion.UUID.String(), status.IID)
	ret := expect == fileName
	if !ret {
		log.Printf("Mismatch between filename and contained uuid/iid: %s vs. %s\n",
			fileName, expect)
	}
	return ret
}

func (status EIDStatus) CheckPendingAdd() bool {
	return status.PendingAdd
}

func (status EIDStatus) CheckPendingModify() bool {
	return status.PendingModify
}

func (status EIDStatus) CheckPendingDelete() bool {
	return status.PendingDelete
}