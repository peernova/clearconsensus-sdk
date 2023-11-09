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
import org.openapitools.client.model.TitaniumRange;

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
 * TitaniumChartRanges
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2023-11-09T10:40:14.901257Z[UTC]")
public class TitaniumChartRanges {
  public static final String SERIALIZED_NAME_BIMODAL_LEFT_POPULATION = "bimodalLeftPopulation";
  @SerializedName(SERIALIZED_NAME_BIMODAL_LEFT_POPULATION)
  private TitaniumRange bimodalLeftPopulation;

  public static final String SERIALIZED_NAME_BIMODAL_RIGHT_POPULATION = "bimodalRightPopulation";
  @SerializedName(SERIALIZED_NAME_BIMODAL_RIGHT_POPULATION)
  private TitaniumRange bimodalRightPopulation;

  public static final String SERIALIZED_NAME_COHORT_CONSENSUS = "cohortConsensus";
  @SerializedName(SERIALIZED_NAME_COHORT_CONSENSUS)
  private TitaniumRange cohortConsensus;

  public static final String SERIALIZED_NAME_EVP = "evp";
  @SerializedName(SERIALIZED_NAME_EVP)
  private TitaniumRange evp;

  public static final String SERIALIZED_NAME_SUBMISSION_EVIDENCE = "submissionEvidence";
  @SerializedName(SERIALIZED_NAME_SUBMISSION_EVIDENCE)
  private TitaniumRange submissionEvidence;

  public static final String SERIALIZED_NAME_SUBMISSION_MIN_MAX = "submissionMinMax";
  @SerializedName(SERIALIZED_NAME_SUBMISSION_MIN_MAX)
  private TitaniumRange submissionMinMax;

  public TitaniumChartRanges() { 
  }

  public TitaniumChartRanges bimodalLeftPopulation(TitaniumRange bimodalLeftPopulation) {
    
    this.bimodalLeftPopulation = bimodalLeftPopulation;
    return this;
  }

   /**
   * Get bimodalLeftPopulation
   * @return bimodalLeftPopulation
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public TitaniumRange getBimodalLeftPopulation() {
    return bimodalLeftPopulation;
  }


  public void setBimodalLeftPopulation(TitaniumRange bimodalLeftPopulation) {
    this.bimodalLeftPopulation = bimodalLeftPopulation;
  }


  public TitaniumChartRanges bimodalRightPopulation(TitaniumRange bimodalRightPopulation) {
    
    this.bimodalRightPopulation = bimodalRightPopulation;
    return this;
  }

   /**
   * Get bimodalRightPopulation
   * @return bimodalRightPopulation
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public TitaniumRange getBimodalRightPopulation() {
    return bimodalRightPopulation;
  }


  public void setBimodalRightPopulation(TitaniumRange bimodalRightPopulation) {
    this.bimodalRightPopulation = bimodalRightPopulation;
  }


  public TitaniumChartRanges cohortConsensus(TitaniumRange cohortConsensus) {
    
    this.cohortConsensus = cohortConsensus;
    return this;
  }

   /**
   * Get cohortConsensus
   * @return cohortConsensus
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public TitaniumRange getCohortConsensus() {
    return cohortConsensus;
  }


  public void setCohortConsensus(TitaniumRange cohortConsensus) {
    this.cohortConsensus = cohortConsensus;
  }


  public TitaniumChartRanges evp(TitaniumRange evp) {
    
    this.evp = evp;
    return this;
  }

   /**
   * Get evp
   * @return evp
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public TitaniumRange getEvp() {
    return evp;
  }


  public void setEvp(TitaniumRange evp) {
    this.evp = evp;
  }


  public TitaniumChartRanges submissionEvidence(TitaniumRange submissionEvidence) {
    
    this.submissionEvidence = submissionEvidence;
    return this;
  }

   /**
   * Get submissionEvidence
   * @return submissionEvidence
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public TitaniumRange getSubmissionEvidence() {
    return submissionEvidence;
  }


  public void setSubmissionEvidence(TitaniumRange submissionEvidence) {
    this.submissionEvidence = submissionEvidence;
  }


  public TitaniumChartRanges submissionMinMax(TitaniumRange submissionMinMax) {
    
    this.submissionMinMax = submissionMinMax;
    return this;
  }

   /**
   * Get submissionMinMax
   * @return submissionMinMax
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public TitaniumRange getSubmissionMinMax() {
    return submissionMinMax;
  }


  public void setSubmissionMinMax(TitaniumRange submissionMinMax) {
    this.submissionMinMax = submissionMinMax;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TitaniumChartRanges titaniumChartRanges = (TitaniumChartRanges) o;
    return Objects.equals(this.bimodalLeftPopulation, titaniumChartRanges.bimodalLeftPopulation) &&
        Objects.equals(this.bimodalRightPopulation, titaniumChartRanges.bimodalRightPopulation) &&
        Objects.equals(this.cohortConsensus, titaniumChartRanges.cohortConsensus) &&
        Objects.equals(this.evp, titaniumChartRanges.evp) &&
        Objects.equals(this.submissionEvidence, titaniumChartRanges.submissionEvidence) &&
        Objects.equals(this.submissionMinMax, titaniumChartRanges.submissionMinMax);
  }

  @Override
  public int hashCode() {
    return Objects.hash(bimodalLeftPopulation, bimodalRightPopulation, cohortConsensus, evp, submissionEvidence, submissionMinMax);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TitaniumChartRanges {\n");
    sb.append("    bimodalLeftPopulation: ").append(toIndentedString(bimodalLeftPopulation)).append("\n");
    sb.append("    bimodalRightPopulation: ").append(toIndentedString(bimodalRightPopulation)).append("\n");
    sb.append("    cohortConsensus: ").append(toIndentedString(cohortConsensus)).append("\n");
    sb.append("    evp: ").append(toIndentedString(evp)).append("\n");
    sb.append("    submissionEvidence: ").append(toIndentedString(submissionEvidence)).append("\n");
    sb.append("    submissionMinMax: ").append(toIndentedString(submissionMinMax)).append("\n");
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
    openapiFields.add("bimodalLeftPopulation");
    openapiFields.add("bimodalRightPopulation");
    openapiFields.add("cohortConsensus");
    openapiFields.add("evp");
    openapiFields.add("submissionEvidence");
    openapiFields.add("submissionMinMax");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

 /**
  * Validates the JSON Object and throws an exception if issues found
  *
  * @param jsonObj JSON Object
  * @throws IOException if the JSON Object is invalid with respect to TitaniumChartRanges
  */
  public static void validateJsonObject(JsonObject jsonObj) throws IOException {
      if (jsonObj == null) {
        if (TitaniumChartRanges.openapiRequiredFields.isEmpty()) {
          return;
        } else { // has required fields
          throw new IllegalArgumentException(String.format("The required field(s) %s in TitaniumChartRanges is not found in the empty JSON string", TitaniumChartRanges.openapiRequiredFields.toString()));
        }
      }

      Set<Entry<String, JsonElement>> entries = jsonObj.entrySet();
      // check to see if the JSON string contains additional fields
      for (Entry<String, JsonElement> entry : entries) {
        if (!TitaniumChartRanges.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TitaniumChartRanges` properties. JSON: %s", entry.getKey(), jsonObj.toString()));
        }
      }
      // validate the optional field `bimodalLeftPopulation`
      if (jsonObj.getAsJsonObject("bimodalLeftPopulation") != null) {
        TitaniumRange.validateJsonObject(jsonObj.getAsJsonObject("bimodalLeftPopulation"));
      }
      // validate the optional field `bimodalRightPopulation`
      if (jsonObj.getAsJsonObject("bimodalRightPopulation") != null) {
        TitaniumRange.validateJsonObject(jsonObj.getAsJsonObject("bimodalRightPopulation"));
      }
      // validate the optional field `cohortConsensus`
      if (jsonObj.getAsJsonObject("cohortConsensus") != null) {
        TitaniumRange.validateJsonObject(jsonObj.getAsJsonObject("cohortConsensus"));
      }
      // validate the optional field `evp`
      if (jsonObj.getAsJsonObject("evp") != null) {
        TitaniumRange.validateJsonObject(jsonObj.getAsJsonObject("evp"));
      }
      // validate the optional field `submissionEvidence`
      if (jsonObj.getAsJsonObject("submissionEvidence") != null) {
        TitaniumRange.validateJsonObject(jsonObj.getAsJsonObject("submissionEvidence"));
      }
      // validate the optional field `submissionMinMax`
      if (jsonObj.getAsJsonObject("submissionMinMax") != null) {
        TitaniumRange.validateJsonObject(jsonObj.getAsJsonObject("submissionMinMax"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TitaniumChartRanges.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TitaniumChartRanges' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TitaniumChartRanges> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TitaniumChartRanges.class));

       return (TypeAdapter<T>) new TypeAdapter<TitaniumChartRanges>() {
           @Override
           public void write(JsonWriter out, TitaniumChartRanges value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TitaniumChartRanges read(JsonReader in) throws IOException {
             JsonObject jsonObj = elementAdapter.read(in).getAsJsonObject();
             validateJsonObject(jsonObj);
             return thisAdapter.fromJsonTree(jsonObj);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of TitaniumChartRanges given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of TitaniumChartRanges
  * @throws IOException if the JSON string is invalid with respect to TitaniumChartRanges
  */
  public static TitaniumChartRanges fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TitaniumChartRanges.class);
  }

 /**
  * Convert an instance of TitaniumChartRanges to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

