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
import org.openapitools.client.model.TitaniumConsensusDensityScore;
import org.openapitools.client.model.TitaniumEvpAlignmentScore;
import org.openapitools.client.model.TitaniumEvpQualityScore;
import org.openapitools.client.model.TitaniumExpertiseScore;

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
 * TitaniumConsensusScores
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2023-06-14T14:50:04.249110Z[UTC]")
public class TitaniumConsensusScores {
  public static final String SERIALIZED_NAME_CONSENSUS_DENSITY_SCORE = "consensusDensityScore";
  @SerializedName(SERIALIZED_NAME_CONSENSUS_DENSITY_SCORE)
  private TitaniumConsensusDensityScore consensusDensityScore;

  public static final String SERIALIZED_NAME_EVP_ALIGNMENT_SCORE = "evpAlignmentScore";
  @SerializedName(SERIALIZED_NAME_EVP_ALIGNMENT_SCORE)
  private TitaniumEvpAlignmentScore evpAlignmentScore;

  public static final String SERIALIZED_NAME_EVP_QUALITY_SCORE = "evpQualityScore";
  @SerializedName(SERIALIZED_NAME_EVP_QUALITY_SCORE)
  private TitaniumEvpQualityScore evpQualityScore;

  public static final String SERIALIZED_NAME_EXPERTISE_SCORE = "expertiseScore";
  @SerializedName(SERIALIZED_NAME_EXPERTISE_SCORE)
  private TitaniumExpertiseScore expertiseScore;

  public TitaniumConsensusScores() { 
  }

  public TitaniumConsensusScores consensusDensityScore(TitaniumConsensusDensityScore consensusDensityScore) {
    
    this.consensusDensityScore = consensusDensityScore;
    return this;
  }

   /**
   * Get consensusDensityScore
   * @return consensusDensityScore
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public TitaniumConsensusDensityScore getConsensusDensityScore() {
    return consensusDensityScore;
  }


  public void setConsensusDensityScore(TitaniumConsensusDensityScore consensusDensityScore) {
    this.consensusDensityScore = consensusDensityScore;
  }


  public TitaniumConsensusScores evpAlignmentScore(TitaniumEvpAlignmentScore evpAlignmentScore) {
    
    this.evpAlignmentScore = evpAlignmentScore;
    return this;
  }

   /**
   * Get evpAlignmentScore
   * @return evpAlignmentScore
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public TitaniumEvpAlignmentScore getEvpAlignmentScore() {
    return evpAlignmentScore;
  }


  public void setEvpAlignmentScore(TitaniumEvpAlignmentScore evpAlignmentScore) {
    this.evpAlignmentScore = evpAlignmentScore;
  }


  public TitaniumConsensusScores evpQualityScore(TitaniumEvpQualityScore evpQualityScore) {
    
    this.evpQualityScore = evpQualityScore;
    return this;
  }

   /**
   * Get evpQualityScore
   * @return evpQualityScore
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public TitaniumEvpQualityScore getEvpQualityScore() {
    return evpQualityScore;
  }


  public void setEvpQualityScore(TitaniumEvpQualityScore evpQualityScore) {
    this.evpQualityScore = evpQualityScore;
  }


  public TitaniumConsensusScores expertiseScore(TitaniumExpertiseScore expertiseScore) {
    
    this.expertiseScore = expertiseScore;
    return this;
  }

   /**
   * Get expertiseScore
   * @return expertiseScore
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public TitaniumExpertiseScore getExpertiseScore() {
    return expertiseScore;
  }


  public void setExpertiseScore(TitaniumExpertiseScore expertiseScore) {
    this.expertiseScore = expertiseScore;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TitaniumConsensusScores titaniumConsensusScores = (TitaniumConsensusScores) o;
    return Objects.equals(this.consensusDensityScore, titaniumConsensusScores.consensusDensityScore) &&
        Objects.equals(this.evpAlignmentScore, titaniumConsensusScores.evpAlignmentScore) &&
        Objects.equals(this.evpQualityScore, titaniumConsensusScores.evpQualityScore) &&
        Objects.equals(this.expertiseScore, titaniumConsensusScores.expertiseScore);
  }

  @Override
  public int hashCode() {
    return Objects.hash(consensusDensityScore, evpAlignmentScore, evpQualityScore, expertiseScore);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TitaniumConsensusScores {\n");
    sb.append("    consensusDensityScore: ").append(toIndentedString(consensusDensityScore)).append("\n");
    sb.append("    evpAlignmentScore: ").append(toIndentedString(evpAlignmentScore)).append("\n");
    sb.append("    evpQualityScore: ").append(toIndentedString(evpQualityScore)).append("\n");
    sb.append("    expertiseScore: ").append(toIndentedString(expertiseScore)).append("\n");
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
    openapiFields.add("consensusDensityScore");
    openapiFields.add("evpAlignmentScore");
    openapiFields.add("evpQualityScore");
    openapiFields.add("expertiseScore");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

 /**
  * Validates the JSON Object and throws an exception if issues found
  *
  * @param jsonObj JSON Object
  * @throws IOException if the JSON Object is invalid with respect to TitaniumConsensusScores
  */
  public static void validateJsonObject(JsonObject jsonObj) throws IOException {
      if (jsonObj == null) {
        if (TitaniumConsensusScores.openapiRequiredFields.isEmpty()) {
          return;
        } else { // has required fields
          throw new IllegalArgumentException(String.format("The required field(s) %s in TitaniumConsensusScores is not found in the empty JSON string", TitaniumConsensusScores.openapiRequiredFields.toString()));
        }
      }

      Set<Entry<String, JsonElement>> entries = jsonObj.entrySet();
      // check to see if the JSON string contains additional fields
      for (Entry<String, JsonElement> entry : entries) {
        if (!TitaniumConsensusScores.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TitaniumConsensusScores` properties. JSON: %s", entry.getKey(), jsonObj.toString()));
        }
      }
      // validate the optional field `consensusDensityScore`
      if (jsonObj.getAsJsonObject("consensusDensityScore") != null) {
        TitaniumConsensusDensityScore.validateJsonObject(jsonObj.getAsJsonObject("consensusDensityScore"));
      }
      // validate the optional field `evpAlignmentScore`
      if (jsonObj.getAsJsonObject("evpAlignmentScore") != null) {
        TitaniumEvpAlignmentScore.validateJsonObject(jsonObj.getAsJsonObject("evpAlignmentScore"));
      }
      // validate the optional field `evpQualityScore`
      if (jsonObj.getAsJsonObject("evpQualityScore") != null) {
        TitaniumEvpQualityScore.validateJsonObject(jsonObj.getAsJsonObject("evpQualityScore"));
      }
      // validate the optional field `expertiseScore`
      if (jsonObj.getAsJsonObject("expertiseScore") != null) {
        TitaniumExpertiseScore.validateJsonObject(jsonObj.getAsJsonObject("expertiseScore"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TitaniumConsensusScores.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TitaniumConsensusScores' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TitaniumConsensusScores> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TitaniumConsensusScores.class));

       return (TypeAdapter<T>) new TypeAdapter<TitaniumConsensusScores>() {
           @Override
           public void write(JsonWriter out, TitaniumConsensusScores value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TitaniumConsensusScores read(JsonReader in) throws IOException {
             JsonObject jsonObj = elementAdapter.read(in).getAsJsonObject();
             validateJsonObject(jsonObj);
             return thisAdapter.fromJsonTree(jsonObj);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of TitaniumConsensusScores given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of TitaniumConsensusScores
  * @throws IOException if the JSON string is invalid with respect to TitaniumConsensusScores
  */
  public static TitaniumConsensusScores fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TitaniumConsensusScores.class);
  }

 /**
  * Convert an instance of TitaniumConsensusScores to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

