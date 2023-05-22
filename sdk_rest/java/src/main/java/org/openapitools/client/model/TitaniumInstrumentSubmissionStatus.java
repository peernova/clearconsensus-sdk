/*
 * clearconsensus-sdk
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.model;

import java.util.Objects;
import java.util.Arrays;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import java.io.IOException;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonArray;
import com.google.gson.JsonDeserializationContext;
import com.google.gson.JsonDeserializer;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParseException;
import com.google.gson.TypeAdapterFactory;
import com.google.gson.reflect.TypeToken;

import java.lang.reflect.Type;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Set;

import org.openapitools.client.JSON;

/**
 * TitaniumInstrumentSubmissionStatus
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2023-05-22T13:06:44.239501Z[UTC]")
public class TitaniumInstrumentSubmissionStatus {
  public static final String SERIALIZED_NAME_CONSENSUS_STATUS = "consensusStatus";
  @SerializedName(SERIALIZED_NAME_CONSENSUS_STATUS)
  private String consensusStatus;

  public static final String SERIALIZED_NAME_CONSENSUS_STATUS_DETAILS = "consensusStatusDetails";
  @SerializedName(SERIALIZED_NAME_CONSENSUS_STATUS_DETAILS)
  private String consensusStatusDetails;

  public static final String SERIALIZED_NAME_HIGHEST_DQE = "highestDqe";
  @SerializedName(SERIALIZED_NAME_HIGHEST_DQE)
  private String highestDqe;

  public static final String SERIALIZED_NAME_PARTICIPANT_CONSENSUS_STATUS = "participantConsensusStatus";
  @SerializedName(SERIALIZED_NAME_PARTICIPANT_CONSENSUS_STATUS)
  private String participantConsensusStatus;

  public static final String SERIALIZED_NAME_PARTICIPANT_CONSENSUS_STATUS_DETAILS = "participantConsensusStatusDetails";
  @SerializedName(SERIALIZED_NAME_PARTICIPANT_CONSENSUS_STATUS_DETAILS)
  private String participantConsensusStatusDetails;

  public TitaniumInstrumentSubmissionStatus() { 
  }

  public TitaniumInstrumentSubmissionStatus consensusStatus(String consensusStatus) {
    
    this.consensusStatus = consensusStatus;
    return this;
  }

   /**
   * Get consensusStatus
   * @return consensusStatus
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getConsensusStatus() {
    return consensusStatus;
  }


  public void setConsensusStatus(String consensusStatus) {
    this.consensusStatus = consensusStatus;
  }


  public TitaniumInstrumentSubmissionStatus consensusStatusDetails(String consensusStatusDetails) {
    
    this.consensusStatusDetails = consensusStatusDetails;
    return this;
  }

   /**
   * Get consensusStatusDetails
   * @return consensusStatusDetails
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getConsensusStatusDetails() {
    return consensusStatusDetails;
  }


  public void setConsensusStatusDetails(String consensusStatusDetails) {
    this.consensusStatusDetails = consensusStatusDetails;
  }


  public TitaniumInstrumentSubmissionStatus highestDqe(String highestDqe) {
    
    this.highestDqe = highestDqe;
    return this;
  }

   /**
   * Get highestDqe
   * @return highestDqe
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getHighestDqe() {
    return highestDqe;
  }


  public void setHighestDqe(String highestDqe) {
    this.highestDqe = highestDqe;
  }


  public TitaniumInstrumentSubmissionStatus participantConsensusStatus(String participantConsensusStatus) {
    
    this.participantConsensusStatus = participantConsensusStatus;
    return this;
  }

   /**
   * Get participantConsensusStatus
   * @return participantConsensusStatus
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getParticipantConsensusStatus() {
    return participantConsensusStatus;
  }


  public void setParticipantConsensusStatus(String participantConsensusStatus) {
    this.participantConsensusStatus = participantConsensusStatus;
  }


  public TitaniumInstrumentSubmissionStatus participantConsensusStatusDetails(String participantConsensusStatusDetails) {
    
    this.participantConsensusStatusDetails = participantConsensusStatusDetails;
    return this;
  }

   /**
   * Get participantConsensusStatusDetails
   * @return participantConsensusStatusDetails
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getParticipantConsensusStatusDetails() {
    return participantConsensusStatusDetails;
  }


  public void setParticipantConsensusStatusDetails(String participantConsensusStatusDetails) {
    this.participantConsensusStatusDetails = participantConsensusStatusDetails;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TitaniumInstrumentSubmissionStatus titaniumInstrumentSubmissionStatus = (TitaniumInstrumentSubmissionStatus) o;
    return Objects.equals(this.consensusStatus, titaniumInstrumentSubmissionStatus.consensusStatus) &&
        Objects.equals(this.consensusStatusDetails, titaniumInstrumentSubmissionStatus.consensusStatusDetails) &&
        Objects.equals(this.highestDqe, titaniumInstrumentSubmissionStatus.highestDqe) &&
        Objects.equals(this.participantConsensusStatus, titaniumInstrumentSubmissionStatus.participantConsensusStatus) &&
        Objects.equals(this.participantConsensusStatusDetails, titaniumInstrumentSubmissionStatus.participantConsensusStatusDetails);
  }

  @Override
  public int hashCode() {
    return Objects.hash(consensusStatus, consensusStatusDetails, highestDqe, participantConsensusStatus, participantConsensusStatusDetails);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TitaniumInstrumentSubmissionStatus {\n");
    sb.append("    consensusStatus: ").append(toIndentedString(consensusStatus)).append("\n");
    sb.append("    consensusStatusDetails: ").append(toIndentedString(consensusStatusDetails)).append("\n");
    sb.append("    highestDqe: ").append(toIndentedString(highestDqe)).append("\n");
    sb.append("    participantConsensusStatus: ").append(toIndentedString(participantConsensusStatus)).append("\n");
    sb.append("    participantConsensusStatusDetails: ").append(toIndentedString(participantConsensusStatusDetails)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }


  public static HashSet<String> openapiFields;
  public static HashSet<String> openapiRequiredFields;

  static {
    // a set of all properties/fields (JSON key names)
    openapiFields = new HashSet<String>();
    openapiFields.add("consensusStatus");
    openapiFields.add("consensusStatusDetails");
    openapiFields.add("highestDqe");
    openapiFields.add("participantConsensusStatus");
    openapiFields.add("participantConsensusStatusDetails");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

 /**
  * Validates the JSON Object and throws an exception if issues found
  *
  * @param jsonObj JSON Object
  * @throws IOException if the JSON Object is invalid with respect to TitaniumInstrumentSubmissionStatus
  */
  public static void validateJsonObject(JsonObject jsonObj) throws IOException {
      if (jsonObj == null) {
        if (TitaniumInstrumentSubmissionStatus.openapiRequiredFields.isEmpty()) {
          return;
        } else { // has required fields
          throw new IllegalArgumentException(String.format("The required field(s) %s in TitaniumInstrumentSubmissionStatus is not found in the empty JSON string", TitaniumInstrumentSubmissionStatus.openapiRequiredFields.toString()));
        }
      }

      Set<Entry<String, JsonElement>> entries = jsonObj.entrySet();
      // check to see if the JSON string contains additional fields
      for (Entry<String, JsonElement> entry : entries) {
        if (!TitaniumInstrumentSubmissionStatus.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TitaniumInstrumentSubmissionStatus` properties. JSON: %s", entry.getKey(), jsonObj.toString()));
        }
      }
      if (jsonObj.get("consensusStatus") != null && !jsonObj.get("consensusStatus").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `consensusStatus` to be a primitive type in the JSON string but got `%s`", jsonObj.get("consensusStatus").toString()));
      }
      if (jsonObj.get("consensusStatusDetails") != null && !jsonObj.get("consensusStatusDetails").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `consensusStatusDetails` to be a primitive type in the JSON string but got `%s`", jsonObj.get("consensusStatusDetails").toString()));
      }
      if (jsonObj.get("highestDqe") != null && !jsonObj.get("highestDqe").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `highestDqe` to be a primitive type in the JSON string but got `%s`", jsonObj.get("highestDqe").toString()));
      }
      if (jsonObj.get("participantConsensusStatus") != null && !jsonObj.get("participantConsensusStatus").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `participantConsensusStatus` to be a primitive type in the JSON string but got `%s`", jsonObj.get("participantConsensusStatus").toString()));
      }
      if (jsonObj.get("participantConsensusStatusDetails") != null && !jsonObj.get("participantConsensusStatusDetails").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `participantConsensusStatusDetails` to be a primitive type in the JSON string but got `%s`", jsonObj.get("participantConsensusStatusDetails").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TitaniumInstrumentSubmissionStatus.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TitaniumInstrumentSubmissionStatus' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TitaniumInstrumentSubmissionStatus> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TitaniumInstrumentSubmissionStatus.class));

       return (TypeAdapter<T>) new TypeAdapter<TitaniumInstrumentSubmissionStatus>() {
           @Override
           public void write(JsonWriter out, TitaniumInstrumentSubmissionStatus value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TitaniumInstrumentSubmissionStatus read(JsonReader in) throws IOException {
             JsonObject jsonObj = elementAdapter.read(in).getAsJsonObject();
             validateJsonObject(jsonObj);
             return thisAdapter.fromJsonTree(jsonObj);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of TitaniumInstrumentSubmissionStatus given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of TitaniumInstrumentSubmissionStatus
  * @throws IOException if the JSON string is invalid with respect to TitaniumInstrumentSubmissionStatus
  */
  public static TitaniumInstrumentSubmissionStatus fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TitaniumInstrumentSubmissionStatus.class);
  }

 /**
  * Convert an instance of TitaniumInstrumentSubmissionStatus to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

